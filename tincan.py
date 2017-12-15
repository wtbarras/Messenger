#!/usr/bin/python3.7
from messenger import Messenger
import messengerutils
from messagethread       import MessageThread
from consoleoutputthread import ConsoleOutputThread
import socket
import queue

def printMenu():
    print("Menu: ")
    print("  s - start tincan node")
    print("  p - print node information")
    print("  q - quit")

def startNode():
    # Create messenger object.
    messenger = Messenger(consoleOutputQueue)
    return messenger

if(__name__ == '__main__'):
    # Create consoleOutputQueue to handle all console output
    consoleOutputQueue = queue.Queue()

    # Make console output thread
    consoleOutputThread = ConsoleOutputThread()
    # Add queue to output from
    consoleOutputThread.setConsoleOutputQueue(consoleOutputQueue)
    consoleOutputThread.start()

    printMenu()

    # Create messenger object.
    messenger = Messenger(consoleOutputQueue)

    # Control loop
    userInput = ''
    while(userInput != "q"):
        userInput = input('')
        if(userInput == 's'):
            startNode()
        elif(userInput == 'p'):
            print("Printing node infomation not yet supported")
        elif(userInput == 'q'):
            pass
        else:
            print("Input not recognized")


    messenger.saveAndExit()
    consoleOutputThread.end()
