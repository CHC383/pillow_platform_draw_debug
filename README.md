# pillow_platform_draw_debug

Reproduction for

## Reproduction

1. Install `uv`
2. Install dependencies: `uv sync`
3. Run image generation script on different platform
   - `./scripts/generate_image.py`.
   - Results will be stored in `./results/<platform>.png`.
4. Compare images
   - `./scripts/diff_image.py ./results/<platform1>.png ./results/<platform2>.png`
   - Results will be stored in `./results/diff_<platform1>_<platform2>.png`.

## Current behavior

Images generated on different OS/platforms are inconsistent; the coordinates are
slightly misaligned.

Results:

- MacOS (Tahoe 26.1): `results/darwin.png`
- Linux (Ubuntu 24.04.3): `results/linux.png`

Diff:

- MacOS vs. Linux: `results/diff_darwin_linux.png`

## Expected behavior

Images generated on different OS/platforms are consistent.
