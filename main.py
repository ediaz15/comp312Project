from flask import Flask, render_template

app = Flask(__name__)


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Booking page
@app.route("/booking")
def booking():
    return render_template("booking.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Policies page
@app.route("/policies")
def policies():
    return render_template("policies.html")


if __name__ == "__main__":
    # host="0.0.0.0" lets Codespaces share it to the browser tab
    app.run(host="0.0.0.0", port=5000, debug=True)
