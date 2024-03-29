from quart import Quart, render_template
import subprocess

app = Quart(__name__)
app.debug = True

tailwind_process = None

async def start_tailwind_cli():
    global tailwind_process
    if app.debug:
        try:
            subprocess.check_output(['pgrep', '-f', './tailwindcss'])
        except subprocess.CalledProcessError:
            print('Starting Tailwind CLI...')
            tailwind_process = subprocess.Popen([
                    './tailwindcss',
                    '-i',
                    'app/static/css/input.css',
                    '-o',
                    'app/static/css/output.css',
                    '--watch',
                ])
            print(tailwind_process)


@app.before_serving
async def before_serving():
    await start_tailwind_cli()


@app.route('/')
async def hello():
    return await render_template('blog/index.html', title='Hello! 👋')

app.run(debug=True)