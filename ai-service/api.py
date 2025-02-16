from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/parse-resume", methods=["POST"])
def parse_resume():
    text = request.json["text"]
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return jsonify(entities)

if __name__ == "__main__":
    app.run(port=5001)
