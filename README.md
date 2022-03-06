# picture-resizer.py

A simple, multi-threaded picture resizing tool leveraging ImageMagick

## Installation

First, [install ImageMagick](https://docs.wand-py.org/en/latest/guide/install.html) on your computer.

Once you have cloned the repository, initialize a virtualenv and install the dependencies:
```bash
python3 -m pip install --user virtualenv #Only if you haven't installed virtualenv yet
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

Then edit the first line of `picture-resizer.py` to match the path
where the project is cloned:
```bash
#!/path/to/picture-resizer/venv/bin/python3
```

Finally, you can either add the file to your `PATH` or setup an `alias` in your
run commands file (ie. `.bashrc`, `zshrc`, etc.)

## Usage

```
picture-resizer.py [-h] --output OUTPUT --width WIDTH [--square] files [files ...]
```

For example, you can resize all JPEGs in a folder (`*.jpg`) to a 2048px (`--width 2048`)
width while keeping their aspect ratio to the `/tmp/export` folder (`--output /tmp/export`):
```
picture-resizer.py --width 2048 --output /tmp/export *.jpg
```

Or you can resize them to square with a white background by adding `--square`:
```
picture-resizer.py --width 2048 --output /tmp/export --square *.jpg
```