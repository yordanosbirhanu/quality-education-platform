# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    answer = request.form.get("answer")
    if answer == "print('Hello World')":
        result = "✅ Correct! Well done."
    else:
        result = "❌ Try again! Hint: Use print('Hello World')."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
