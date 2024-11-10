import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class GitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ignore changes in the .git directory
        if '.git' in event.src_path:
            return

        # Proceed with adding, committing, and pushing changes
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Auto-commit: Updated files"])
        subprocess.run(["git", "push"])

if __name__ == "__main__":
    path = "E:/EVERYDAY_DSA_PPROBLEMS"
    event_handler = GitHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
