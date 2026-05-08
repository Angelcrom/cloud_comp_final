# cloud_comp_final - Campus Event Aggregator

# Cloud Services Used

- Cloud Functions
- Pub/Sub
- Eventarc
- Firestore
- Flask web application
- Cloud Run

# Data Flow

1. A message is published to the Pub/Sub topic “event-topic”

2. Pub/Sub triggers Eventarc

3. Eventarc routes the event to the Cloud Function “generate_event”

4. The Cloud Function generates a fake campus event with:

   - event_1 (first part of event title)
   - event_2 (second part of event title)
   - date
   - time
   - location

5. The function writes the new event document into Firestore under a “events” collection

6. The Flask application queries Firestore and shows all stored events in the browser

# Final Architecture Diagram

Pub/Sub -> Eventarc -> Cloud Function -> Firestore -> Flask UI
