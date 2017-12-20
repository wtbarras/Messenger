import messengerutils
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread
import socket
import queue

class Messenger:

    def __init__(self, consoleOutputQueue, server_port):
        self.output_queue = consoleOutputQueue
        self.port = server_port
        self.messageThreadDict = dict()

    # Generate server thread and begin listening for connections
    def start(self):
        # @TODO Implement messenger.start() method
        self.output_queue.put("serverthread needs to be implemented before a node can be started")
        pass

    # Output data about message node and associated server and message threads
    def print_data():
        pass

    # Create and Initialize messageThread with default parameters
    def generate_message_thread(self):
        mt = MessageThread(0)
        # Give it a consoleOutputQueue so it can speak
        try:
            mt.setConsoleOutputQueue(self.output_queue)
        except NameError:
            # If a consoleOutputQueue hasn't been passed to this messenger,
            #   then we can't add it to the message thread
            # @TODO Make a custom error to raise for this
            pass
        self.messageThreadDict[mt.getAddress()] = mt
        self.output_queue.put("message threads open " + str(len(self.messageThreadDict)) )
        mt.start()

    def set_console_output_thread(self, consoleOutputQueue):
        self.output_queue = consoleOutputQueue

    def save_and_exit(self):
        # Eventually this will do more than just call another function
        self.output_queue.put("message threads to close " + str(len(self.messageThreadDict)))
        try:
            self.close_message_threads()
        except AttributeError:
            # Can't close threads that aren't there
            print("Error when trying to close message threads: There are no message threads")
            pass
        self.output_queue.put("message threads open " + str(len(self.messageThreadDict)))

    def close_message_threads(self):
        while( len(self.messageThreadDict) != 0):
            print("Calling.end on thread")
            threadTuple = self.messageThreadDict.popitem()
            threadTuple[1].end()
