from flask import Flask, render_template
from src.routes import default
import sys

PRODUCTION = len(sys.argv) > 1

app = Flask(__name__)

app.add_url_rule('/',           view_func=default.home)
app.add_url_rule('/robots.txt', view_func=default.robots)
app.add_url_rule('/edit',       view_func=default.editor)

@app.route('/example')
def give_example():
    e = render_template('pages/example.html')
    return e

if __name__ == '__main__':
    if not PRODUCTION:
        app.run(debug=True)
    else:
        port = sys.argv[1]
        app.run(host='0.0.0.0', port=port)