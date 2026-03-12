from flask import Flask, render_template, request

app = Flask(__name__)

genre = [
"lofi chill beat",
"lofi hip hop beat",
"jazzy lofi beat",
"ambient lofi beat",
"dreamy lofi beat"
]

instrument = [
"soft piano",
"electric piano",
"mellow guitar",
"rhodes piano",
"lofi synth pad",
"acoustic guitar"
]

drum = [
"soft boom bap drum",
"dusty hip hop drum",
"minimal chill drum",
"warm analog drum",
"light jazz drum groove"
]

texture = [
"vinyl crackle",
"tape saturation",
"warm analog texture",
"dusty cassette sound",
"vintage lofi filter"
]

ambience = [
"rain ambience",
"night city ambience",
"coffee shop ambience",
"fireplace ambience",
"forest ambience",
"ocean wave ambience"
]

tempo = [
"slow tempo 60 bpm",
"chill tempo 70 bpm",
"relaxed tempo 75 bpm",
"smooth tempo 80 bpm"
]

purpose = [
"studying",
"relaxing",
"sleeping",
"reading",
"focus work"
]

@app.route("/", methods=["GET","POST"])
def index():

    prompt = ""

    if request.method == "POST":

        g = request.form.get("genre")
        i = request.form.get("instrument")
        d = request.form.get("drum")
        t = request.form.get("texture")
        a = request.form.get("ambience")
        te = request.form.get("tempo")
        p = request.form.get("purpose")

        prompt = f"""
{g} instrumental lofi beat,
{i} melody,
{d} groove,
{t},
{a},
{te},
background music for {p},
no vocals
""".strip()

    return render_template("index.html",
        genre=genre,
        instrument=instrument,
        drum=drum,
        texture=texture,
        ambience=ambience,
        tempo=tempo,
        purpose=purpose,
        prompt=prompt
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)