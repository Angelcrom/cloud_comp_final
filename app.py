from flask import Flask, render_template, request, redirect
from google.cloud import firestore

app = Flask(__name__)

db = firestore.Client()

@app.route("/")
def home():
    events_ref = db.collection("events").stream()

    events = []
    for doc in events_ref:
        event = doc.to_dict()
        event["id"] = doc.id   # <-- IMPORTANT
        events.append(event)

    return render_template("index.html", events=events)

@app.route("/delete/<doc_id>", methods=["POST"])
def delete_event(doc_id):
    db.collection("events").document(doc_id).delete()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)