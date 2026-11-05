"""Checks every pack listed in index.json the way the Lumetra app does.
Run: python3 tools/validate.py  (exit 1 on any problem)."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = {"blackAndWhiteNegative", "colorNegative", "slide"}
problems = []

def cited(entry, name):
    c = entry.get("citation") or {}
    if not str(c.get("title", "")).strip():
        problems.append(f"{name}: every entry needs citation.title, where the numbers came from")

def film(f, where):
    name = f"{where} film {f.get('name') or f.get('id')}"
    for key in ("id", "name", "manufacturer", "iso", "kind", "reciprocity"):
        if key not in f: problems.append(f"{name}: missing {key}")
    if f.get("kind") not in KINDS: problems.append(f"{name}: kind must be one of {sorted(KINDS)}")
    if not 6 <= float(f.get("iso", 0)) <= 25600: problems.append(f"{name}: iso out of range")
    r = f.get("reciprocity") or {}
    m = r.get("model")
    if m == "schwarzschild":
        if not 1 <= float(r.get("p", 0)) <= 2: problems.append(f"{name}: p must be 1 to 2")
    elif m == "table":
        pts = r.get("points") or []
        if len(pts) < 2 or any(len(p) != 2 or p[0] <= 0 or p[1] < p[0] for p in pts):
            problems.append(f"{name}: table needs two or more [metered, corrected] pairs")
    elif m != "none":
        problems.append(f"{name}: reciprocity.model must be schwarzschild, table or none")
    cited(f, name)

def kit(k, where):
    name = f"{where} kit {k.get('name') or k.get('id')}"
    for key in ("id", "name", "fastest", "slowest", "bulb"):
        if key not in k: problems.append(f"{name}: missing {key}")
    if not 0 < k.get("fastest", 0) < k.get("slowest", 0) <= 3600: problems.append(f"{name}: shutter range not valid")
    w, s = k.get("widest"), k.get("smallest")
    if (w is None) != (s is None) or (w is not None and not 0.7 <= w < s <= 256):
        problems.append(f"{name}: give both widest and smallest, widest the smaller f-number")
    if "shutterSteps" in k and k["shutterSteps"] not in ("full", "half", "third"):
        problems.append(f"{name}: shutterSteps must be full, half or third")
    if "mount" in k and not (isinstance(k["mount"], str) and k["mount"].strip()):
        problems.append(f"{name}: mount must be a name such as Canon FD")
    cited(k, name)

index = json.load(open(os.path.join(ROOT, "index.json")))
ids = set()
for entry in index.get("packs", []):
    path = entry.get("file", "")
    if ".." in path or not path.endswith(".json"):
        problems.append(f"index: bad file name {path}"); continue
    pack = json.load(open(os.path.join(ROOT, path)))
    for f in pack.get("films", []):
        film(f, path)
        if f.get("id") in ids: problems.append(f"{path}: id {f.get('id')} is used twice")
        ids.add(f.get("id"))
    for k in pack.get("kits", []):
        kit(k, path)
        if k.get("id") in ids: problems.append(f"{path}: id {k.get('id')} is used twice")
        ids.add(k.get("id"))

print("\n".join(problems) or f"OK: {len(ids)} entries")
sys.exit(1 if problems else 0)
