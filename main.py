#!/usr/bin/env python3
"""Copy the newspaper front-page image into the output directory.

Reads entry.png from the directory containing this script, copies it to
/output/entry.png (creating /output when it does not exist yet), and
prints the SHA-256 digest of the copied file.
"""

import hashlib
import os
import shutil
import sys


EXPECTED_SHA256 = "002ebf04dcbf3ef595cd57cced211d19810760dc82d53d904a15b4c0441333fd"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    target = os.path.join("/output", "entry.png")

    shutil.copyfile(source, target)
    result = sha256_of(target)
    print(result)
    if result != EXPECTED_SHA256:
        print(
            f"sha256 mismatch: expected {EXPECTED_SHA256}, got {result}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
