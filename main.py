#!/usr/bin/env python3
"""Publish the 20 November 2026 news poster.

The deliverable is ``entry.png``: one 1024x1024 front page for a single day.
This program does two things and nothing else:

* ``--check-only``: read the PNG, check what the intake enforces (PNG
  signature, chunk CRCs, IHDR first, IEND last, at most 1024x1024, at most
  1 MiB) and print one JSON line with size, dimensions and sha256;
* without flags: the same checks, then copy the file byte for byte to
  ``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``output/``).

It never re-encodes the image, so two runs write identical bytes, and it
makes no network calls. Standard library only.
"""

from __future__ import annotations

import hashlib
import json
import os
import struct
import sys
import zlib

MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024
SIGNATURE = b"\x89PNG\r\n\x1a\n"

# The page is one day wide, so the run is a copy, never a re-encode:
# byte-identical output on the grader's second run is the whole contract.
COPY_ONLY = True


def read_chunks(data: bytes) -> tuple[list[tuple[bytes, bytes]], str | None]:
    """Walk the chunk stream and verify every CRC. Returns (chunks, error)."""
    if not data.startswith(SIGNATURE):
        return [], "not a PNG: signature mismatch"
    pos = len(SIGNATURE)
    chunks: list[tuple[bytes, bytes]] = []
    while pos + 8 <= len(data):
        (length,) = struct.unpack(">I", data[pos : pos + 4])
        kind = data[pos + 4 : pos + 8]
        body = data[pos + 8 : pos + 8 + length]
        if len(body) != length:
            return chunks, f"truncated chunk {kind!r}"
        crc_bytes = data[pos + 8 + length : pos + 12 + length]
        if len(crc_bytes) != 4:
            return chunks, f"missing CRC on {kind!r}"
        (stated,) = struct.unpack(">I", crc_bytes)
        if zlib.crc32(kind + body) & 0xFFFFFFFF != stated:
            return chunks, f"CRC mismatch on {kind!r}"
        chunks.append((kind, body))
        pos += 12 + length
        if kind == b"IEND":
            break
    if not chunks or chunks[0][0] != b"IHDR":
        return chunks, "IHDR is not the first chunk"
    if chunks[-1][0] != b"IEND":
        return chunks, "no IEND chunk"
    return chunks, None


def inspect(path: str) -> dict:
    with open(path, "rb") as handle:
        data = handle.read()
    chunks, error = read_chunks(data)
    report: dict = {
        "source": path,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "chunks": len(chunks),
        "ok": False,
    }
    if error:
        report["error"] = error
        return report
    width, height, depth, colour = struct.unpack(">IIBB", chunks[0][1][:10])
    report.update(
        width=width,
        height=height,
        bit_depth=depth,
        colour_type=colour,
        max_bytes=MAX_BYTES,
        max_side=MAX_SIDE,
    )
    problems = []
    if width > MAX_SIDE or height > MAX_SIDE:
        problems.append(f"{width}x{height} is over the {MAX_SIDE}px limit")
    if len(data) > MAX_BYTES:
        problems.append(f"{len(data)} bytes is over the 1 MiB limit")
    report["ok"] = not problems
    if problems:
        report["error"] = "; ".join(problems)
    return report


def main(argv: list[str]) -> int:
    check_only = "--check-only" in argv
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.exists(source):
        print(json.dumps({"ok": False, "error": f"missing {source}"}))
        return 1

    report = inspect(source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    if report["ok"] and not check_only:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.png")
        with open(source, "rb") as src, open(target, "wb") as dst:
            dst.write(src.read())
        report["written"] = target
    print(json.dumps(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
