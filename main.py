#!/usr/bin/env python3
"""Publish the news poster: validate entry.png, then copy it to /output/entry.png.

Standard library only, no network, deterministic. The grader runs the program
twice and both runs must write the same bytes, so the image is passed through
untouched: nothing here re-encodes, rescales or rewrites it.

Usage:
    python3 main.py                 validate, then copy into $MAKEFUN_OUTPUT_DIR
    python3 main.py --check-only    validate and print one JSON object, write nothing
    python3 main.py --summary       the same report as --check-only, write nothing
    python3 main.py --list-chunks   print one JSON object per PNG chunk, write nothing
    python3 main.py --strict        also require at least 32768 bytes

Exit status is 0 on success and 2 on any defect, reported as a single JSON line
on stderr. --list-chunks prints one object per line ("type", "length", "crc").
"""

from __future__ import annotations

import hashlib
import json
import os
import struct
import sys
import tempfile
import zlib
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ENTRY_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024
STRICT_MIN_BYTES = 32768
MAX_CHUNK_BYTES = 0x7FFFFFFF

# IHDR colour type -> the bit depths PNG allows for it (PNG spec, table 11.1).
ALLOWED_DEPTHS = {0: (1, 2, 4, 8, 16), 2: (8, 16), 3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}
FLAGS = {"--check-only": "check_only", "--summary": "summary",
         "--list-chunks": "list_chunks", "--strict": "strict"}


def emit(payload: dict, stream=None) -> None:
    """Print one compact, key-sorted JSON object on a single line."""
    line = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    print(line, file=stream or sys.stdout)


def fail(reason: str, **detail) -> None:
    """The single failure path: one JSON line on stderr, exit 2, no traceback."""
    payload = {"ok": False, "reason": reason}
    payload.update(detail)
    emit(payload, sys.stderr)
    raise SystemExit(2)


def parse_args(argv: list[str]) -> dict:
    flags = {name: False for name in FLAGS.values()}
    for argument in argv:
        name = FLAGS.get(argument)
        if name is None:
            fail("unknown_argument", argument=argument, allowed=sorted(FLAGS))
        flags[name] = True
    return flags


def read_entry(path: Path) -> bytes:
    if not path.is_file():
        fail("missing_entry", path=str(path), expected=ENTRY_NAME)
    try:
        return path.read_bytes()
    except OSError as exc:
        fail("entry_unreadable", path=str(path), error=exc.strerror or str(exc))


def read_chunks(data: bytes) -> list[dict]:
    """Walk every chunk, checking framing and the CRC-32 of each one."""
    if len(data) < len(PNG_SIGNATURE) or data[: len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        fail("bad_signature", bytes=len(data))
    chunks: list[dict] = []
    offset = len(PNG_SIGNATURE)
    total = len(data)
    while offset < total:
        if offset + 8 > total:
            fail("truncated_chunk_header", offset=offset)
        length = struct.unpack(">I", data[offset : offset + 4])[0]
        raw_type = data[offset + 4 : offset + 8]
        if length > MAX_CHUNK_BYTES:
            fail("chunk_too_long", offset=offset, length=length)
        body_end = offset + 8 + length
        if body_end + 4 > total:
            fail("truncated_chunk", offset=offset,
                 type=raw_type.decode("latin-1"), length=length)
        stored = struct.unpack(">I", data[body_end : body_end + 4])[0]
        computed = zlib.crc32(data[offset + 4 : body_end]) & 0xFFFFFFFF
        if computed != stored:
            fail("bad_crc", offset=offset, type=raw_type.decode("latin-1"),
                 length=length, stored=stored, computed=computed)
        chunk_type = raw_type.decode("latin-1")
        chunks.append({"type": chunk_type, "length": length, "crc": stored, "offset": offset})
        offset = body_end + 4
        if chunk_type == "IEND":
            if length != 0:
                fail("bad_iend", length=length)
            if offset != total:
                fail("trailing_bytes", offset=offset, extra=total - offset)
            return chunks
    fail("missing_iend", chunks=len(chunks))


def read_header(data: bytes, chunks: list[dict]) -> dict:
    """IHDR must come first, be 13 bytes, and describe an image we accept."""
    if not chunks or chunks[0]["type"] != "IHDR":
        fail("missing_ihdr", first=chunks[0]["type"] if chunks else None)
    if chunks[0]["length"] != 13:
        fail("bad_ihdr", length=chunks[0]["length"])
    start = chunks[0]["offset"] + 8
    width, height, depth, color, compression, filtering, interlace = struct.unpack(
        ">IIBBBBB", data[start : start + 13]
    )
    if width == 0 or height == 0:
        fail("empty_image", width=width, height=height)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        fail("too_many_pixels", width=width, height=height, limit=MAX_DIMENSION)
    if color not in ALLOWED_DEPTHS or depth not in ALLOWED_DEPTHS[color]:
        fail("bad_pixel_format", bit_depth=depth, color_type=color)
    if compression != 0 or filtering != 0 or interlace not in (0, 1):
        fail("bad_ihdr_method", compression=compression,
             filtering=filtering, interlace=interlace)
    return {
        "width": width,
        "height": height,
        "bit_depth": depth,
        "color_type": color,
        "interlace": interlace,
    }


def validate(path: Path, strict: bool) -> tuple[dict, bytes]:
    data = read_entry(path)
    size = len(data)
    if size > MAX_BYTES:
        fail("too_large", bytes=size, limit=MAX_BYTES)
    if strict and size < STRICT_MIN_BYTES:
        fail("too_small", bytes=size, minimum=STRICT_MIN_BYTES, strict=True)
    chunks = read_chunks(data)
    header = read_header(data, chunks)
    if not any(chunk["type"] == "IDAT" for chunk in chunks):
        fail("missing_idat", chunks=len(chunks))
    report = {
        "ok": True,
        "source": str(path),
        "bytes": size,
        "sha256": hashlib.sha256(data).hexdigest(),
        "chunks": len(chunks),
        "crc": "ok",
        "iend": True,
        "strict": strict,
    }
    report.update(header)
    return report, data


def publish(data: bytes, output_dir: str) -> str:
    """Write the bytes beside the target, then swap them in with os.replace."""
    directory = Path(output_dir)
    try:
        directory.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        fail("output_not_writable", directory=str(directory), error=exc.strerror or str(exc))
    target = directory / ENTRY_NAME
    temporary = None
    try:
        handle, temporary = tempfile.mkstemp(prefix=".entry-", suffix=".png", dir=str(directory))
        os.fchmod(handle, 0o644)
        with os.fdopen(handle, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
        temporary = None
    except OSError as exc:
        fail("output_not_writable", path=str(target), error=exc.strerror or str(exc))
    finally:
        if temporary is not None and os.path.exists(temporary):
            try:
                os.unlink(temporary)
            except OSError:
                pass
    return str(target)


def main(argv: list[str]) -> None:
    flags = parse_args(argv)
    source = Path(__file__).resolve().parent / ENTRY_NAME
    report, data = validate(source, flags["strict"])
    if flags["list_chunks"]:
        for chunk in read_chunks(data):
            emit({"type": chunk["type"], "length": chunk["length"], "crc": chunk["crc"]})
    if flags["check_only"] or flags["summary"]:
        report["written"] = False
        emit(report)
        return
    if flags["list_chunks"]:
        return
    target = publish(data, os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    report["written"] = True
    report["target"] = target
    emit(report)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except SystemExit:
        raise
    except Exception as exc:  # one line, never a traceback
        fail("unexpected_error", error=f"{type(exc).__name__}: {exc}")
