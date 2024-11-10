import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call

# Path to the directory you want to monitor
watch_directory = "E:/EVERYDAY_DSA_PPROBLEMS"

# Git commands
def git_commit_push():
    try:
        call(["git", "add", "."])
        call(["git", "commit", "-m", "Auto-commit changes"])
        call(["git", "push"])
    except Exception as e:
        print(f"Error with git commands: {e}")

# Event handler
class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"File {event.src_path} has been modified")
        git_commit_push()

    def on_created(self, event):
        print(f"File {event.src_path} has been created")
        git_commit_push()

    def on_deleted(self, event):
        print(f"File {event.src_path} has been deleted")
        git_commit_push()

    def on_moved(self, event):
        print(f"File {event.src_path} has been moved to {event.dest_path}")
        git_commit_push()

# Main function to set up the observer
def main():
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_directory, recursive=True)
    observer.start()
    print("Monitoring started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring stopped.")
    observer.join()

if __name__ == "__main__":
    main()
