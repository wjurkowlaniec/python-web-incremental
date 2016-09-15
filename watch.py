from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from subprocess import call
import time
import os

from subprocess import Popen
class PythonOnlyHandler(PatternMatchingEventHandler):
    patterns = ['*.py'] # filenames to process
    def process(self,event):
        for f in self.patterns:
            Popen("transcrypt {}".format(event.src_path), shell=True, env=os.environ)

    def on_modified(self, event):
        print (event)
        self.process(event)


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(PythonOnlyHandler(), path='.')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
