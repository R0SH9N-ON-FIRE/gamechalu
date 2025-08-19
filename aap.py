from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    target = random.choice(['🎯', '👾', '🧟', '💣', '🛸'])
    if request.method == "POST":
        action = request.form.get("action")
        if action == "shoot":
            hit = random.choice([True, False])
            result = "💥 Hit! Target down." if hit else "😵 Missed! Target bach gaya."
        elif action == "skip":
            result = "😐 Skip kiya. Agla target..."
    return render_template("index.html", target=target, result=result)

if __name__ == "__main__":
    app.run(debug=True)
