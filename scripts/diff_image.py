#!/usr/bin/env -S uv run --script

from pathlib import Path
import sys

from PIL import Image, ImageChops

ROOT_PATH = Path(__file__).parent.parent.absolute()


def main(img1_path: Path, img2_path: Path) -> None:
    with Image.open(img1_path) as img1, Image.open(img2_path) as img2:
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox(alpha_only=False):
            output_path = (
                ROOT_PATH / "results" / f"diff_{img1_path.stem}_{img2_path.stem}.png"
            )
            diff.save(output_path)
        else:
            print("Images are identical.")


if __name__ == "__main__":
    main(img1_path=Path(sys.argv[1]), img2_path=Path(sys.argv[2]))
