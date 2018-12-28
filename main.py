from flask import Flask, render_template
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)
