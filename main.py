from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

potato_family = {
    "potato": "potato.png",
    "French Fries": "French-Fries.png",
    "Blue Swede": "blueswede.jpg",
    "Chips": "chips.png",
    "Sweet Potato": "Sweet-Potato.png"
}

def generateRandomPotato():
    potato_familyName = list(potato_family.keys())
    random_potato = random.choice(potato_familyName)
    potato_familyFile = potato_family[random_potato]
    return potato_familyName, random_potato, potato_familyFile

@app.route("/", methods=["POST", "GET"])
def home(): 
    potato_familyName, random_potato, potato_familyFile = generateRandomPotato()

    if request.method == "POST":
        if request.form.get("button_a"): 
            potato_familyName, random_potato, potato_familyFile = generateRandomPotato()
    return render_template('index.html', potatoName = random_potato, potatoFile = potato_familyFile)

if __name__ == "__main__":
    app.run(debug=True)