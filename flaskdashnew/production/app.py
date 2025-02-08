import flask
from flask import render_template, redirect, url_for

app = flask.Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True

@app.route("/dashboard")
def home():
    return render_template("index2_2.html")
@app.route("/<name>")
def user(name):
    return f"Hello-- {name}!"
@app.route("/admin")
def admin():
    return redirect(url_for("dashboard"))
	
if __name__ == '__main__':
    app.run(host="localhost", port=5004, debug=True)