import os
from pathlib import Path

from PIL import Image

MEDIA_ROOT = str(
    Path(__file__).resolve(strict=True).parent.parent.parent / "nftguru" / "media"
)


def merge(files):

    j = 0
    while j < len(files):
        fileName = str(files[j])
        if j == 0:
            background = Image.open(files[j])
            foreground = Image.open(files[j + 1])
            j = j + 2
        else:
            foreground = Image.open(files[j])
            j = j + 1

        bg_w, bg_h = background.size
        fg_w, fg_h = foreground.size

        background = Image.alpha_composite(
            Image.new("RGBA", background.size), background.convert("RGBA")
        )
        offset = ((bg_w - fg_w) // 2, (bg_h - fg_h) // 2)
        background.paste(foreground, offset, foreground)

    background.save(os.path.join(MEDIA_ROOT, "merged.webp"))

    return background
