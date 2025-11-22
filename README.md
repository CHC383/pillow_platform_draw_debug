# pillow_platform_draw_debug

Reproduction for https://github.com/python-pillow/Pillow/issues/9307

## Reproduction

1. Install `uv`
2. Install dependencies: `uv sync`
3. Run image generation script on different platform
   - (MacOS/Linux): `./scripts/generate_image.py`
   - (Windows): `uv run .\scripts\generate_image.py`
   - Results will be stored in `./results/<platform>.png`.
4. Compare images
   - (MacOS/Linux):
     `./scripts/diff_image.py ./results/<platform1>.png ./results/<platform2>.png`
   - (Windows):
     `uv run .\scripts\diff_image.py .\results\<platform1>.png .\results\<platform2>.png`
   - Results will be stored in `./results/diff_<platform1>_<platform2>.png`.

## Current behavior

Images generated on different OS/platforms are inconsistent; the coordinates are
slightly misaligned.

Results:

- MacOS (Tahoe 26.1): `results/darwin.png`
- Linux (Ubuntu 24.04.3): `results/linux.png`
- Windows (Windows 11): `results/windows.png`

Diff (Ran on MacOS):

- MacOS vs. Linux: `results/diff_darwin_linux.png`
- MacOS vs. Windows:
  - Original: `results/diff_darwin_windows.png`
  - Level adjusted: `results/diff_darwin_windows_level_adjusted.png`
- Linux vs. Linux: `results/diff_linux_windows.png`

## Expected behavior

Images generated on different OS/platforms are consistent.
