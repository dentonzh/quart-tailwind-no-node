This is a no-frills [Quart](https://quart.palletsprojects.com/en/latest/index.html) project starter that allows you to use Tailwind without Node.



## Clone this repository

By using git via command line: `git clone https://github.com/dentonzh/quart-tailwind-no-node.git`
Or by [downloading the zip](https://github.com/dentonzh/quart-tailwind-no-node/archive/refs/heads/main.zip)

## Download Tailwind's standalone CLI

Select the correct executable from [the list of exectuables (under "Assets")](https://github.com/tailwindlabs/tailwindcss/releases) based on your OS and architecture.

Rename this executable to `tailwindcss`.

If on Linux or Mac, run `chmod +x tailwindcss` to make `tailwindcss` executable.

## Set up virtualenv and install dependencies

Via command line: `python -m venv path/to/new/virtual/environment`
Followed by this command: `pip install -r requirements.txt`

## Run your project

Via command line: `quart run`

Note that `app/__init__.py` contains code that runs the `tailwindcss` executable. When you make changes to any of the templates in `app/templates`, `tailwindcss` will automatically compile a new `output.css` file.

## Minify output.css for production

To minify your `output.css` for production, run this command:

`./tailwindcss -i app/static/css/input.css -o app/static/css/output.css --minify`

