import time
import logging
from watchdog.observers import Observer
  
from watchdog.events import FileSystemEventHandler
from Classifier import classify_event
 


# Logging setup
logging.basicConfig(
    filename='file_monitoring.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("FileMonitoringAgent")       # typo fixed: "FileMonitoingAgent"

class FileMonitoringHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            classification = classify_event(event)
            logger.info(f"{classification}: {event.src_path}")
            print(f"{classification}: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            classification = classify_event(event)
            logger.info(f"{classification}: {event.src_path}")
            print(f"{classification}: {event.src_path}")

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


if __name__ == "__main__":   # indentation fixed
    path = "."  # directory to monitor
    event_handler = FileMonitoringHandler()   # typo fixed: "MyHandler" → "FileMonitoringHandler"
    observers = Observer()
    observers.schedule(event_handler, path, recursive=True)
    observers.start()

    logger.info("File Monitoring Agent started...")

    try:
        while True:
            time.sleep(1)  # keep the script running
    except KeyboardInterrupt:
        observers.stop()
        logger.info("File Monitoring Agent stopped.")
    observers.join()
