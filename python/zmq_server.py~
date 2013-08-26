#SKumar

import zmq
from random import choice

def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://127.0.0.1:5001')
    print 'Hello, World'
    my_states = ['TN','KA','KL','AP']
    heroes = ['Rajini','Kamal','Chiranjeevi','Mammutti']
    i = 0
    while True:
        if i >= 10:
            print 'Exiting'
            break
        msg = choice(my_states) + ' - ' + choice(heroes)
        print msg
        socket.send(msg)
        #i += 1

if __name__ == '__main__':
    main()

