import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from AGENT.Classifier import classify_event
from REGEX.detector import detect_sensitive_data

# Logging setup
logging.basicConfig(
    filename='file_monitoring.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("FileMonitoringAgent")

class FileMonitoringHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and not event.src_path.endswith("file_monitoring.log"):
            classification = classify_event(event)
            logger.info(f"{classification}: {event.src_path}")
            print(f"{classification}: {event.src_path}")

            findings = detect_sensitive_data(event.src_path)
            if findings:
                for label, matches in findings:
                    logger.warning(f"SENSITIVE {label} detected in {event.src_path}: {matches}")
                    print(f"SENSITIVE {label} detected in {event.src_path}: {matches}")

    def on_modified(self, event):
        if not event.is_directory and not event.src_path.endswith("file_monitoring.log"):
            classification = classify_event(event)
            logger.info(f"{classification}: {event.src_path}")
            print(f"{classification}: {event.src_path}")

            findings = detect_sensitive_data(event.src_path)
            if findings:
                for label, matches in findings:
                    logger.warning(f"SENSITIVE {label} detected in {event.src_path}: {matches}")
                    print(f"SENSITIVE {label} detected in {event.src_path}: {matches}")

    def on_deleted(self, event):
        if not event.is_directory:
            classification = classify_event(event)
            logger.info(f"{classification}: {event.src_path}")
            print(f"{classification}: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            classification = classify_event(event)
            logger.info(f"{classification}: from {event.src_path} to {event.dest_path}")
            print(f"{classification}: from {event.src_path} to {event.dest_path}")

            findings = detect_sensitive_data(event.src_path)
            if findings:
                for label, matches in findings:
                    logger.warning(f"SENSITIVE {label} detected in {event.src_path}: {matches}")
                    print(f"SENSITIVE {label} detected in {event.src_path}: {matches}")

if __name__ == "__main__":
    path = "."
    event_handler = FileMonitoringHandler()
    observers = Observer()
    observers.schedule(event_handler, path, recursive=True)
    observers.start()

    logger.info("File Monitoring Agent started...")

    # One-time sanity check at startup
    results = detect_sensitive_data("AGENT/test_file.txt")
    print("Startup scan:", results)

    try:
        while True:
            time.sleep(0.1)  # faster loop
    except KeyboardInterrupt:
        observers.stop()
        logger.info("File Monitoring Agent stopped.")
    observers.join()
