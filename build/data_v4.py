# -*- coding: utf-8 -*-
"""v4 data: 16 main boxes + 50 one-line briefs, all first reported Friday 20 Nov 2026."""

DAY = "Friday 20 November 2026"

NUMBERS = [
    ("300,000", "evacuated in Odisha"),
    ("423", "rescue teams deployed"),
    ("−4.49%", "Nikkei, Friday close"),
    ("118", "Phillips' runs off 193 balls"),
    ("50", "stories on this page"),
    ("3,551", "gold an ounce, down 3.65%"),
]

# (no, region, kicker, headline, body, source)
CARDS = [
    (1, 'ASIA', 'STORM',
     'Akvan comes ashore at Gopalpur',
     'Akvan crossed near Gopalpur between 07:30 and 08:30 IST. Over 300,000 evacuated, 423 rescue teams out; Odisha reported no untoward incident.',
     'India Today · The Hindu'),
    (2, 'ASIA', 'MARKETS',
     "AI fears drag Asia's markets down",
     "The Nikkei fell 4.49% to 56,775.04, its lowest since April, as Anthropic's debut failed to calm AI worries. Topix −3.12%; Kospi −4.5%.",
     'AP · Kyodo · Mainichi'),
    (3, 'ASIA', 'DIPLOMACY',
     'Delhi opens the first SCO forum',
     'Modi opened the first SCO Civilisational Dialogue Forum: three days of scholars and cultural delegates from member states.',
     'PIB / Akashvani'),
    (4, 'ASIA', 'SPACE',
     'Mitsubishi Heavy takes the H3',
     'Mitsubishi Heavy takes over H3 launches from JAXA from rocket No. 11 next year, science minister Yoshihiro Seki said.',
     'Kyodo News'),
    (5, 'EUROPE', 'BREXIT',
     'Burnham seals the Brussels reset',
     'Burnham signed post-Brexit deals on youth exchanges, food trade and emissions trading. Tuition fees remain the last snag.',
     'POLITICO · The Guardian'),
    (6, 'EUROPE', 'WAR',
     'Russia fires missiles across Ukraine',
     'Russia fired missiles and drones across Ukraine overnight into Friday, Tu-160 bombers reported, after strikes on central Kyiv.',
     'Kyiv Independent · The Defense Post'),
    (7, 'EUROPE', 'INDUSTRY',
     'Lufthansa cuts 1,000 jobs as metalworkers strike',
     'Lufthansa plans to cut 1,000 jobs, German media reported, as IG Metall began 24-hour warning strikes nationwide.',
     'tagesschau'),
    (8, 'AMERICAS', 'FLOOD',
     "Florida's record flood keeps climbing",
     'The St Johns River held above its all-time record at Cocoa and was forecast to rise again. Flooding could last into 2027.',
     'AccuWeather'),
    (9, 'AMERICAS', 'WASHINGTON',
     'White House fires its cyber chief',
     'Sean Cairncross was ousted as cyber director after a week of outages, from a Microsoft failure to 18,000 grounded flights.',
     'RNZ · The Hindu'),
    (10, 'AFRICA', 'POLITICS',
     "Kenya's opposition walks out on IEBC",
     'The opposition walked out of IEBC talks with five "non-negotiable" demands, deepening a standoff over Kenya\'s next election.',
     'Daily Nation'),
    (11, 'OCEANIA', 'CRICKET',
     'Phillips century grinds India down',
     'Phillips made 118 off 193 balls as New Zealand were bowled out for 368 — the first with Test, ODI and T20I hundreds against India in a year.',
     'The Hindu · Hindustan Times'),
    (12, 'MIDEAST', 'HORMUZ',
     'Three versions of one Hormuz attack',
     "Iran's army, navy and Revolutionary Guard gave three accounts of one mine attack in the eastern strait. No hull was confirmed.",
     'Iran File'),
    (13, 'MIDEAST', 'CLIMATE',
     'COP31 runs to its last day',
     'The Antalya draft was cut from 18 pages to 9, fossil-fuel language gone and no binding commitments added, as 198 countries talked on.',
     'la Repubblica · UN News'),
    (14, 'EUROPE', 'JUSTICE',
     'The ICJ ruling draws its first answers',
     'The EU told Myanmar to comply "without delay"; Britain expelled its defence attaché. Myanmar called the ruling unfair.',
     'Anadolu · Africanews'),
    (15, 'EUROPE', 'ENLARGEMENT',
     'Hungary lifts its veto on Ukraine',
     "Budapest was set to drop its veto on Ukraine's last two accession clusters, two diplomatic sources said, unblocking Moldova.",
     'Euronews'),
    (16, 'AFRICA', 'RIGHTS',
     'Tunisian activist sentenced to five years',
     "Sihem Bensedrine, former head of Tunisia's truth commission, was sentenced to five years, her lawyer said.",
     'Africanews'),
]

# (no, text, source)
BRIEFS = [
    (17, 'Myanmar rejects ICJ ruling', 'Africanews'),
    (18, 'Activists protest COP31 outcome', 'Africanews'),
    (19, 'Benin seeks 35 looted pieces', 'Africanews'),
    (20, 'Somali march backs UAE expulsion', 'Africanews'),
    (21, 'One child in four in war zones', 'Save the Children'),
    (22, 'Malawi fuel queues empty pumps', 'Al Jazeera'),
    (23, 'Laos studies 1,275-MW wind farm', 'Vientiane Times'),
    (24, 'Chiang Mai opens 15-stop e-bus', 'The Nation'),
    (25, 'AI agents to pay bills via AXS', 'Straits Times'),
    (26, 'BIMSTEC aid for Nepal, Bhutan', 'Global New Light'),
    (27, 'Court allows one-time temple lamp', 'The Hindu'),
    (28, 'Singapore weighs retrenchment aid', 'CNA'),
    (29, 'Gold −3.65% to $3,551 an ounce', 'Rio Times'),
    (30, 'Peso slides 3.61% to 3,427', 'Rio Times'),
    (31, 'Ibovespa −0.69%, IPC −0.38%', 'Rio Times'),
    (32, 'Rupee gains 17 paise to 93.15', 'The Hindu'),
    (33, 'Jharkhand shuts primary classes', 'The Hindu'),
    (34, 'Fire emissions third-highest', 'Copernicus'),
    (35, 'BOLO list: Goldy Brar, C$250,000', 'The Hindu'),
    (36, 'Honda Avancier due spring 2027', 'Kyodo'),
    (37, 'Trump briefs Takaichi on call', 'Kyodo'),
    (38, 'Tashima joins FIFA race', 'Kyodo'),
    (39, 'Vietnam hosts APEC in 2027', 'Viet Nam News'),
    (40, 'Mexico screens foreign takeovers', 'DOF'),
    (41, 'Kenyan milk output falls again', 'Daily Nation'),
    (42, 'Rand weakest in a year, JSE slides', 'Business Day'),
    (43, 'Congress alleges ₹1,211 crore scam', 'Indian Express'),
    (44, 'Court restores dropped voters', 'Indian Express'),
    (45, "China's envoy: Nepal a priority", 'Khabarhub'),
    (46, 'M5.6 quake, Loyalty Islands', 'Earthquake Track'),
    (47, 'Haiti police kill 34 in raid', 'Anadolu'),
    (48, 'Wong and Xi meet in Shenzhen', 'CNA'),
    (49, 'Ex-Awami MP held in Satkhira', 'Dhaka Observer'),
    (50, 'UK shuts 8 more asylum hotels', 'Anadolu'),
]

TIMELINE = [
    ("00:00", "COP31's slimmed 9-page draft circulates in Antalya"),
    ("00:49", "M5.6 quake southeast of the Loyalty Islands, depth 10 km"),
    ("01:48", "Hormuz traffic listed \"restricted\" after the tanker claims"),
    ("02:30", "Tokyo's morning session closes with the Nikkei down 4.5%"),
    ("07:30", "Cyclone Akvan begins crossing near Gopalpur"),
    ("11:00", "EU ambassadors move to lift Hungary's veto on Ukraine"),
]

MARKETS = [
    ("NIKKEI", "56,775.04", "−4.49%", "dn"),
    ("KOSPI", "4,905.20", "−4.50%", "dn"),
    ("HANG SENG", "22,393.93", "−2.00%", "dn"),
    ("BRENT", "$90.11", "−2.03%", "dn"),
    ("GOLD", "$3,551", "−3.65%", "dn"),
    ("USD/COP", "3,427", "+3.61%", "up"),
]

DATECHECK = [
    "Anthropic closed at $97.17, up 17%",
    "Senate rejected the Iran war powers, 48–51",
    "Kyiv: Austrian and Dutch embassies hit",
    "Somalia expels the UAE ambassador",
    "GTA VI: 19.05m copies on day one",
    "Tonga declares a 27-day emergency",
    "Houthi missile hits the PIF tower",
    "Xi, Putin and Trump sign a declaration",
    "ICJ: Myanmar committed genocide",
    "Mongolia's president resigns",
    "Indonesia passes asset forfeiture law",
    "Seoul: Han Duck-soo retrial ordered",
]

SOURCES = ("India Today · The Hindu · AP · PIB · Kyodo · POLITICO · The Guardian · "
           "Kyiv Independent · The Defense Post · tagesschau · AccuWeather · RNZ · Daily Nation · "
           "Hindustan Times · Iran File · la Repubblica · UN News · Euronews · Anadolu · Africanews · "
           "Al Jazeera · Bernama · CNA · Dhaka Observer · Khabarhub · Viet Nam News · DOF · Tennis Canada · "
           "The Athletic · Indian Express · Mainichi · Business Day · The Queenslander · Earthquake Track · "
           "Sarabangla · Copernicus · Rio Times")
