echo "Deleting Cloud Function..."
gcloud functions delete generate_event \
  --gen2 \
  --region=us-central1 \
  --quiet

echo "Deleting Pub/Sub topic..."
gcloud pubsub topics delete event-topic

echo "Deleting project.."
gcloud projects delete helical-bonsai-495507-h6