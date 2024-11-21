import zmq
import time

run = False
context = zmq.Context()
socket = context.socket(zmq.REP)


def start_runner():
    run = True
    socket.bind("tcp://*:5555")
    while run:
        message = socket.recv()
        print("Received request: %s" % message)

        time.sleep(1)

        socket.send(b"World")
