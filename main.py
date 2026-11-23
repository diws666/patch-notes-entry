# Real-Life Patch Notes entry: a terse release note for a bug in human biology
# (the clicking knee). Written verbatim to /output/entry.txt.
import os

ENTRY = "v2.4.1: fixed a bug where your knee clicks every time you stand up. Knee now ships silent."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
