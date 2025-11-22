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

## Expected behavior
