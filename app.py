from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = None
    if request.method == "POST":
        disease = request.form.get("disease")
        info = model.get(disease)
        if info:
            suggestion = {
                "eat": info['foods_to_eat'],
                "avoid": info['foods_to_avoid']
            }
    return render_template("index.html", suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
