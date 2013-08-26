#SKumar
import zmq

def main():
    print 'Hello, World'
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:5001')
    socket.setsockopt(zmq.SUBSCRIBE, "TN")
    #socket.setsockopt(zmq.SUBSCRIBE, "")
    while True:
        print socket.recv()

if __name__ == '__main__':
    main()

