import unittest
import socket
import sys
sys.path.insert(0, './../')
import messagethread


class TestMessageThreadMethods(unittest.TestCase):

    def test_default_socket_family(self):
        mThread = messagethread.MessageThread()
        socketFamily = mThread.socket.family
        self.assertEqual(socketFamily, socket.AF_INET)
        mThread.closeSocket()

    def test_default_socket_type(self):
        mThread = messagethread.MessageThread()
        socketType = mThread.socket.type
        self.assertEqual(socketType, socket.SOCK_STREAM)
        mThread.closeSocket()

if __name__ == '__main__':
    unittest.main()
