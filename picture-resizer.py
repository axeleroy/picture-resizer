#!/home/axel/PycharmProjects/picture-resizer/venv/bin/python3
import argparse
import os
import threading
from math import ceil

from wand.color import Color
from wand.image import Image


def arg_parsing():
    """Parses the arguments given to the script and returns them."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--square", action='store_true')
    parser.add_argument("files", nargs='+', default=[])

    return parser.parse_args()


def resize_picture(source: Image, output: str, extension: str, output_width: int, square: bool):
    with source.clone() as img:
        if square is True:
            width = float(img.width)
            height = float(img.height)
            border_height = 0
            border_width = 0
            if width > height:
                crop_size = int(width)
                border_height = int(ceil((width - height) / 2))
            else:
                crop_size = int(height)
                border_width = int(ceil((height - width) / 2))
            img.border(color=Color('white'), height=border_height, width=border_width)
            img.crop(top=0, left=0, width=crop_size, height=crop_size)

        img.transform(resize=f'{output_width}x')
        img.save(filename=f'{output}{extension}')

        return img.format, img.width, img.height


def open_and_resize_picture(filepath: str):
    print(f"Resizing {filepath}")
    filename, file_extension = os.path.splitext(os.path.basename(filepath))
    output_path = f'{args.output}/{filename}'
    with Image(filename=filepath) as picture:
        picture.auto_orient()
        resize_picture(picture, output_path, file_extension, args.width, args.square)
        print(f"Done resizing {filepath}")


args = arg_parsing()
if not os.path.isdir(args.output):
    print(f'ERROR: {args.output} is not a folder')
    exit(1)


for path in args.files:
    threading.Thread(target=open_and_resize_picture(path))
