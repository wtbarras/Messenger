import socket
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread

def parseUserInput(userInput):
    if(userInput == 'q'):
        saveAndExit

# Sets up a message thread with a default port and the specified
#   consoleOutputQueue. At some point, this should probably be a factory or something
# @TODO make a factory class to create message thread objects
def initMessageThread(consoleOutputQueue):
    # Make server thread
    thread = MessageThread()
    # Initialize thread with default settings
    thread.init()
    # Tell the thread where to send console output
    thread.setConsoleOutputQueue(consoleOutputQueue)
    return thread

def saveAndExit(server, outputQueue):
    server.end()
    outputQueue.end()
    pass
