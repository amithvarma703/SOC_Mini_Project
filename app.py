
from flask import Flask, render_template
from detection.rules import detect_bruteforce

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("logs/auth.log") as f:
        logs = f.readlines()
    alerts = detect_bruteforce(logs)
    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
