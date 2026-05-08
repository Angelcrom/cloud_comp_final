from google.cloud import firestore
import base64
import json
import random
from datetime import datetime

db = firestore.Client()

def generate_event(event, contextls):
    event_1 = [
        "Campus",
        "Tech",
        "Music",
        "Study",
        "Game",
    ]

    event_2 = ["Bingo", "Talk", "Jam", "Social", "Party"]

    location = ["UC Commons", "The Oval", "Adam Center", "UC Ballroom"]

    date = ["2026-05-7", "2026-05-8", "2026-05-9", "2026-05-10", "2026-05-11", "2026-05-12", "2026-05-13"]

    time = ["10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm"]


    event = {
        "event_1": random.choice(event_1),
        "event_2": random.choice(event_2),
        "location": random.choice(location),
        "date": random.choice(date),
        "time": random.choice(time),
        "created_at": datetime.utcnow()
    }

    db.collection("events").add(event)

    return "Event added!", 200