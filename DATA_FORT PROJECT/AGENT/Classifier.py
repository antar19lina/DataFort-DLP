# Classifier.py
def classify_event(event):   # lowercase c
    if event.event_type == "created":
        return "File created"
    elif event.event_type == "modified":
        return "File modified"
    elif event.event_type == "deleted":
        return "File deleted"
    else:
        return "Unknown event type"
