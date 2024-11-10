import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class GitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ignore changes in the .git directory
        if '.git' in event.src_path:
            return

        # Proceed with adding, committing, and pushing changes for modified or added files
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Auto-commit: Updated files"])
        subprocess.run(["git", "push"])

    def on_deleted(self, event):
        # Ignore changes in the .git directory
        if '.git' in event.src_path:
            return

        # Proceed with adding, committing, and pushing changes for deleted files
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Auto-commit: Deleted file {event.src_path}"])
        subprocess.run(["git", "push"])

    def on_created(self, event):
        # Ignore changes in the .git directory
        if '.git' in event.src_path:
            return

        # Proceed with adding, committing, and pushing changes for new files
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Auto-commit: Added new file {event.src_path}"])
        subprocess.run(["git", "push"])

if __name__ == "__main__":
    # Path to your project directory
    path = "E:/EVERYDAY_DSA_PPROBLEMS"
    
    # Initialize the observer and handler
    event_handler = GitHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    
    # Start monitoring
    observer.start()
    
    print(f"Monitoring {path} for changes. Press Ctrl+C to stop.")
    
    try:
        # Keep the script running indefinitely
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring stopped.")
    observer.join()
