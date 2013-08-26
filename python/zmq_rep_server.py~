#SKumar
import time
import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://localhost:5555')
    print 'Hello,'
    while True:        
        message = socket.recv()
        print 'Message received is : %s'%message
        socket.send("World")
        
    
if __name__ == '__main__':
    main()