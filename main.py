from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

potato_family = {
    "potato": "potato.png",
    "French Fries": "French-Fries.png",
    "Blue Swede": "blueswede.jpg",
    "Chips": "chips.png",
    "Sweet Potato": "Sweet-Potato.png"
}

potato_familyName = list(potato_family.keys())
random_potato = random.choice(potato_familyName)
potato_familyFile = potato_family[random_potato]

@app.route("/")
def home():
    
    return render_template('index.html', potatoName = potato_familyName, potatoFile = potato_familyFile)

if __name__ == "__main__":
    app.run(debug=True)