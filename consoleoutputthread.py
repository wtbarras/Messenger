from threading import Thread
import queue

class ConsoleOutputThread(Thread):

    def setConsoleOutputQueue(self, q):
        self.consoleOutputQueue = q

    def run(self):
        self.keepRunning = 1
        while(self.keepRunning == 1):
            try:
                # Try to print whatever is on top of the queue
                print(self.consoleOutputQueue.get(True, .001))
                # Print prompt after every line so users know input can be accepted
                print("$", end='', flush=True)
            except:
                # We do not care if this is empty.
                pass

    def end(self):
        self.keepRunning = 0
