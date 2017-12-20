from threading import Thread
import socket

class ServerThread(Thread):

    def __init__(self, port_param, console_output_queue_param, messenger_param):
        # Messenger object that this ServerThread is associated with
        self.messenger = messenger_param

        # Queue that holds strings that will be output. Handled by ConsoleOutputThread
        self.console_output_queue = console_output_queue_param

        # Set port to listen on
        self.port = port_param
        # The port has to be greater than 1024
        # @TODO Add error if port less than 1024
        if(self.port <= 1024):
            self.console_output_queue.put("Error: Port needs to be greater than 1024")

        # Set up socket that will be used as the connection point for incoming
        #   comminucations.
        # Make socket for server thread to listen on
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind socket to specified port and address.
        self.server_socket.bind((socket.gethostname(), self.port))


    def run(self):
        # Begin listening for incoming connections
        self.server_socket.listen()
        # @TODO Implement blocking listen in ServerThread.run
