from quart import Quart, render_template
import subprocess

app = Quart(__name__)
app.debug = True

@app.before_serving
def run_tailwind_cli():
    if app.debug:
        subprocess.Popen(
            [
                './tailwindcss',
                '-i',
                'app/static/css/input.css',
                '-o',
                'app/static/css/output.css',
                '--watch',
            ]
        )

@app.route('/')
async def hello():
    return await render_template('blog/index.html', title='Hello! 👋')

app.run(debug=True)