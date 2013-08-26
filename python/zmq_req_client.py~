#SKumar

import zmq

def main():
    context = zmq.Context()
    socket  = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')
    for req in range(10):
        print 'hello'
        print 'Sending Request %d'%req
        socket.send('Hello')
        message = socket.recv()
        print 'Got reply for ',req, '[ ',message, ']'
        
if __name__ == '__main__':
    main()