from threading import Thread
import socket
import queue

class MessageThread(Thread):

    # Initialize messageThread with default settings
    # @TODO This needs to be named somethng other than init. That one is taken
    def __init__(self, threadId, socketFamily=socket.AF_INET, socketType=socket.SOCK_STREAM):
        # Init superclass
        Thread.__init__(self)
        self.id = threadId
        # Make socket for server thread to listen on
        s = socket.socket(socketFamily, socketType)
        # Socket for thread to listen on
        self.setSocket(s)
        # Create variable

    def setConsoleOutputQueue(self, q):
        self.consoleOutputQueue = q

    # Method: run
    # Parameters: self
    # Purpose: This method is where the thread begins execution
      # It will loop while listening on a socket for incoming messages
    def run(self):
        self.outputWithId("Thread Started!")
        # Bind the socket to a port.
        # Have to use a port greater than 1024 if this is going to run as a non-sudo user
        # Add the id to it so if there are multiple threads, they are on different ports
        self.message_socket.bind((socket.gethostname(), 4477 + self.id))
        # Begin listening for incoming connections
        self.message_socket.listen()
        self.outputWithId("Listening on: " + str(self.getAddress()) + " : " + str(self.getPort()))
        self.keepRunning = 1
        # @TODO make this loop as AbstractEventLoop object
        while(self.keepRunning == 1):
            pass

    def end(self):
        print("closing message thread")
        self.keepRunning = 0

    def closeSocket(self):
        self.message_socket.close()

    def setMessageQueue(self, queue):
        self.queue = queue

    def setSocket(self, s):
        self.message_socket = s;

    def getAddress(self):
        return self.message_socket.getsockname()[0]

    def getPort(self):
        return self.message_socket.getsockname()[1]

    def outputWithId(self, outputString):
        self.consoleOutputQueue.put(str(self.id) + ">> " + outputString)
