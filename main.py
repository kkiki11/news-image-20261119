from hashlib import sha256
from pathlib import Path
from shutil import copyfile
import sys

WANTED = "002ebf04dcbf3ef595cd57cced211d19810760dc82d53d904a15b4c0441333fd"


def run() -> int:
    origin = Path(__file__).resolve().parent / "entry.png"
    target = Path("/output/entry.png")
    target.parent.mkdir(parents=True, exist_ok=True)
    copyfile(origin, target)
    digest = sha256(target.read_bytes()).hexdigest()
    print(f"sha256: {digest}")
    if digest != WANTED:
        print(f"error: sha256 mismatch: expected {WANTED}, got {digest}", file=sys.stderr)
        return 1
    return 0


raise SystemExit(run())
