from messenger import Messenger
import messengerutils
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread
import socket
import queue



if(__name__ == '__main__'):
    # Create consoleOutputQueue to handle all console output
    consoleOutputQueue = queue.Queue()

    # Make console output thread
    consoleOutputThread = ConsoleOutputThread()
    # Add queue to output from
    consoleOutputThread.setConsoleOutputQueue(consoleOutputQueue)
    consoleOutputThread.start()

    # Create messenger object.
    messenger = Messenger(consoleOutputQueue)

    # Create a messageThread to listen on
    messenger.generateMessageThread()

    # Control loop
    userInput = ''
    while(userInput != "q"):
        userInput = input('')

    messenger.saveAndExit()
    consoleOutputThread.end()
