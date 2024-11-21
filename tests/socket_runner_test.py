import zmq
import unittest
from threading import Thread
from time import sleep

from backend.socket.socket_runner import start_runner


class TestRunner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Starting runner")
        cls.runner_thread = Thread(target=start_runner, daemon=True)
        cls.runner_thread.start()
        sleep(1)

    def test_fetch_greeting_request(self):
        print("Connecting to hello world server...")
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        for request in range(10):
            print("Sending request %s ..." % request)
            socket.send(b"Hello")

            message = socket.recv()
            sleep(1)
            print("Received reply %s [%s]" % (request, message))
            self.assertEqual(b"World", message)

    @classmethod
    def tearDownClass(cls):
        """Clean up resources."""
        # ZeroMQ doesn't need explicit server teardown due to daemon thread
        pass


if __name__ == "__main__":
    unittest.main()
