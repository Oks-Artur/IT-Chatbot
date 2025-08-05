from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Chatbot-Logik ---
def get_response(user_input):
    user_input = user_input.lower()  # Wandelt die Eingabe in Kleinbuchstaben um

    if "hallo" in user_input:
        return "Hallo! Wie kann ich dir helfen?"

    elif "warum bin ich" in user_input and ("der ideale kandidat" in user_input or "für diesen ausbildungsplatz" in user_input):
        return ("BMW ist ein innovatives Unternehmen mit Fokus auf IT und Digitalisierung. "
                "Du wärst der passende Kandidat für diese Stelle, da du sehr lernbereit bist "
                "und zusammen mit der BMW Group als idealen Arbeitgeber wachsen möchtest!")

    elif "danke" in user_input or "vielen dank" in user_input:
        return "Gerne doch!"

    else:
        return "Das habe ich leider nicht verstanden."

# --- Routen ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    response = get_response(data["message"])
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)

