import messengerutils
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread
import socket
import queue

class Messenger:

    def __init__(self, consoleOutputQueue):
        self.outputQueue = consoleOutputQueue
        self.messageThreadDict = dict()

    # Create and Initialize messageThread with default parameters
    def generateMessageThread(self):
        mt = MessageThread()
        # Give it a consoleOutputQueue so it can speak
        try:
            mt.setConsoleOutputQueue(self.outputQueue)
        except NameError:
            # If a consoleOutputQueue hasn't been passed to this messenger,
            #   then we can't add it to the message thread
            # @TODO Make a custom error to raise for this
            pass
        self.messageThreadDict[mt.getAddress()] = mt
        self.outputQueue.put("message threads open " + str(len(self.messageThreadDict)) )
        mt.start()

    def setConsoleOutputThread(self, consoleOutputQueue):
        self.outputQueue = consoleOutputQueue

    def saveAndExit(self):
        # Eventually this will do more than just call another function
        self.outputQueue.put("message threads to close " + str(len(self.messageThreadDict)))
        try:
            self.closeMessageThreads()
        except AttributeError:
            # Can't close threads that aren't there
            print("Goddamn")
            pass
        self.outputQueue.put("message threads open " + str(len(self.messageThreadDict)))

    def closeMessageThreads(self):
        while( len(self.messageThreadDict) != 0):
            print("Calling.end on thread")
            threadTuple = self.messageThreadDict.popitem()
            threadTuple[1].end()
