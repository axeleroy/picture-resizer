# picture-resizer.py

A simple, multi-threaded picture resizing tool leveraging ImageMagick

## Installation

First, [install ImageMagick](https://docs.wand-py.org/en/latest/guide/install.html) on your computer.

Once you have cloned the repository, initialize a virtualenv and install the dependencies:
```bash
python3 -m pip install --user virtualenv # Only if you haven't installed virtualenv yet
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

To make your life easier, you should create an alias for picture-resizer:
```bash
alias picture-resizer='/path/to/picture-resizer/env/bin/python3 /path/to/picture-resizer/picture-resizer.py'
```

## Usage

```
picture-resizer [-h] --output OUTPUT --width WIDTH [--square] files [files ...]
```

For example, you can resize all JPEGs in a folder (`*.jpg`) to a 2048px (`--width 2048`)
width while keeping their aspect ratio to the `/tmp/export` folder (`--output /tmp/export`):
```
picture-resizer --width 2048 --output /tmp/export *.jpg
```

Or you can resize them to square with a white background by adding `--square`:
```
picture-resizer --width 2048 --output /tmp/export --square *.jpg
```
