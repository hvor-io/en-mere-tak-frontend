from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(ssl_context='adhoc', host='0.0.0.0')
