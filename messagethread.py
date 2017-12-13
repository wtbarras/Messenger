from threading import Thread
import socket
import queue

class MessageThread(Thread):

    def setSocket(self, s):
        self.socket = s;

    # Initialize messageThread with default settings
    # @TODO This needs to be named somethng other than init. That one is taken
    def __init__(self, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM):
        # Init superclass
        Thread.__init__(self)
        # Make socket for server thread to listen on
        s = socket.socket(socketFamily, socketType)
        # Socket for thread to listen on
        self.setSocket(s)
        # Create variable

    def setConsoleOutputQueue(self, q):
        self.consoleOutputQueue = q

    def run(self):
        # print("Thread started!")
        self.consoleOutputQueue.put("Thread Started!")
        self.keepRunning = 1
        # @TODO make this loop as AbstractEventLoop object
        while(self.keepRunning == 1):
            pass

    def end(self):
        print("closing message thread")
        self.keepRunning = 0


    def setMessageQueue(self, queue):
        self.queue = queue

    def getAddress(self):
        # @TODO return actual address from getAddress
        self.address = 1
        return self.address
