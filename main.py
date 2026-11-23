#!/usr/bin/env python3
"""Entry runner for news-image-20261122.

Copies the poster image.png next to this script to the output directory
(default /output, or MAKEFUN_OUTPUT_DIR when set) and verifies the copy
byte-for-byte: SHA-256 and file size must match the source, and the PNG
must be exactly 1024x1024.

Python 3.13, standard library only, no network.
"""
import hashlib
import os
import shutil
import struct
import sys

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256_file(path):
    """Return the hex SHA-256 digest of a file."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_png_dimensions(path):
    """Return (width, height) from a PNG file, or None if invalid."""
    with open(path, "rb") as fh:
        header = fh.read(33)
    if len(header) < 33 or header[:8] != PNG_SIGNATURE:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def validate_png(path):
    """Check PNG signature, first chunk IHDR, and exact dimensions.

    Returns (width, height) on success, or None with an error message.
    """
    try:
        dims = read_png_dimensions(path)
    except OSError as exc:
        return None, f"cannot read source image: {exc}"
    if dims is None:
        return None, "source image is not a valid PNG (bad signature or IHDR)"
    if dims != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        return None, (
            f"source dimensions {dims[0]}x{dims[1]} != "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    return dims, None


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.png")

    if not os.path.isfile(source):
        return fail(f"source image not found: {source}")

    dims, error = validate_png(source)
    if error is not None:
        return fail(error)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output directory {out_dir}: {exc}")
    dest = os.path.join(out_dir, "entry.png")

    try:
        shutil.copyfile(source, dest)
    except OSError as exc:
        return fail(f"copy failed: {exc}")

    src_size = os.path.getsize(source)
    dst_size = os.path.getsize(dest)
    if src_size != dst_size:
        return fail(f"size mismatch: source {src_size} != output {dst_size}")

    src_hash = sha256_file(source)
    dst_hash = sha256_file(dest)
    if src_hash != dst_hash:
        return fail("SHA-256 mismatch between source and output")

    print(f"output: {dest}")
    print(f"sha256: {dst_hash}")
    print(f"size: {dst_size} bytes")
    print(f"dimensions: {dims[0]}x{dims[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
