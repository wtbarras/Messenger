#!/usr/bin/python3.7
from messenger import Messenger
import messengerutils
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread

import sys
import socket
import queue

def printMenu():
    print("Menu: ")
    print("  s - start tincan node")
    print("  p - print node information")
    print("  q - quit")

def startNode(messenger, port):
    messenger.start()
    return messenger

if(__name__ == '__main__'):
    # If a port was specified, use that. If not, default to 4477
    if(sys.argv[1] == '-p'):
        unparsed_port = sys.argv[2]
        port = int(unparsed_port)
    else:
        port = 4477

    # Create consoleOutputQueue to handle all console output
    consoleOutputQueue = queue.Queue()

    # Make console output thread
    consoleOutputThread = ConsoleOutputThread()
    # Add queue to output from
    consoleOutputThread.setConsoleOutputQueue(consoleOutputQueue)
    consoleOutputThread.start()

    # Create messenger object.
    messenger = Messenger(consoleOutputQueue, port)

    # Print menu to command line
    printMenu()

    # Control loop
    userInput = ''
    while(userInput != "q"):
        userInput = input('')
        if(userInput == 's'):
            startNode(messenger, port)
        elif(userInput == 'p'):
            messenger.print_data()
        elif(userInput == 'q'):
            pass
        else:
            print("Input not recognized")


    messenger.save_and_exit()
    consoleOutputThread.end()
