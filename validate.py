#!/usr/bin/env python3
"""Checks cases.json before it is published. Same rules as the app's CaseDataTest.
Usage: python3 validate.py [cases.json]   (exit code 0 = OK)"""
import json, re, sys
from datetime import datetime

path = sys.argv[1] if len(sys.argv) > 1 else "cases.json"
data = json.load(open(path, encoding="utf-8"))
fails = []

# Victims, witnesses and others who were never charged, named in source articles. Never put these in case text.
# Add to this list whenever a new article names someone who was not charged.
UNCHARGED = ["Vargas", "Daniels", "Bowman", "Percy", "Dorian", "Shaun", "Shaw", "Van Love", "Holmes", "Richie",
             "Lewis", "Marissa", "Clenelle", "Hill", "Young", "Eric", "Arron", "Castro", "Haffer", "Demarko",
             "Farrar", "Michael Hill", "Richard"]
FIELDS = ["id", "date", "area", "title", "outcome", "kind", "happened", "claim", "ended", "note"]

try:
    datetime.strptime(data["checked"].strip(), "%b %d, %Y")
except Exception:
    fails.append('"checked" must look like "Nov 5, 2026"')

cases = data.get("cases", [])
if not cases:
    fails.append("no cases")
ids = set()
for c in cases:
    cid = c.get("id", "?")
    for f in FIELDS:
        if not isinstance(c.get(f), str) or not c[f].strip():
            fails.append(f"{cid}: missing or empty {f}")
    text = " ".join(str(c.get(f, "")) for f in FIELDS if f not in ("id", "kind"))
    for n in UNCHARGED:
        if re.search(r"\b" + re.escape(n) + r"\b", text):
            fails.append(f"{cid}: names uncharged person '{n}'")
    if cid in ids:
        fails.append(f"{cid}: duplicate id")
    ids.add(cid)
    if c.get("kind") not in ("cleared", "convicted", "mixed", "open"):
        fails.append(f"{cid}: kind must be cleared, convicted, mixed or open")
    srcs = c.get("sources") or []
    if not srcs:
        fails.append(f"{cid}: no sources")
    for s in srcs:
        if not str(s.get("title", "")).strip() or not str(s.get("url", "")).startswith("https://"):
            fails.append(f"{cid}: each source needs a title and an https:// url")

for f in fails:
    print("FAIL", f)
print(f"{len(cases)} cases; checked {data.get('checked')}")
print("ALL PASS" if not fails else f"{len(fails)} FAILED")
sys.exit(1 if fails else 0)
