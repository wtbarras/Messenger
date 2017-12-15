import unittest
import socket
import sys
sys.path.insert(0, './../')
import messagethread


class TestMessageThreadMethods(unittest.TestCase):

    def test_default_socket_family(self):
        mThread = messagethread.MessageThread(0)
        socketFamily = mThread.message_socket.family
        self.assertEqual(socketFamily, socket.AF_INET)
        mThread.closeSocket()

    def test_default_socket_type(self):
        mThread = messagethread.MessageThread(0)
        socketType = mThread.message_socket.type
        self.assertEqual(socketType, socket.SOCK_STREAM)
        mThread.closeSocket()

    def test_getAddress(self):
        mThread = messagethread.MessageThread(0)
        mThread.message_socket.bind((socket.gethostname(), 4477))
        self.assertEqual(mThread.getAddress(), socket.gethostbyname(socket.gethostname()))

    def test_getPort(self):
        mThread = messagethread.MessageThread(0)
        mThread.message_socket.bind((socket.gethostname(), 4477))
        self.assertEqual(mThread.getPort(), 4477)

if __name__ == '__main__':
    unittest.main()
