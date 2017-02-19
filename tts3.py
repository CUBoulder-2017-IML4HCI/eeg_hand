import OSC
import time
import os
import socket
import numpy as np


array = []
current_output = 1.0
count = 0
not_count = 0

UDP_IP = "127.0.0.1"
UDP_PORT = 8200
addr = '127.0.0.1',8200

weki_address = '127.0.0.1', 6448
weki = OSC.OSCClient()
weki.connect(weki_address)

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.bind((UDP_IP,UDP_PORT))
s = OSC.OSCServer(addr)
#s.addDefaultHandlers()
s.timeout = 0
run = True

loop_element = 0

arg_buffer = np.empty((5, 10))


def handle_timeout(self):
    self.timed_out = True

import types
s.handle_timeout = types.MethodType(handle_timeout, s)

def response(path,tags, args, source):
    global arg_buffer
    global count
    global not_count
    global current_output

    if count >= 10:
        msg = OSC.OSCMessage()
        msg.setAddress("/wek/inputs")
        send_vals = [None] * 5
        count = 0
        for i in xrange(5):
            #print 'arg_buffer[' + str(i) + '] ' + str(arg_buffer[i])
            send_vals[i] = np.mean(arg_buffer[i])
            msg.append(send_vals[i])
        weki.send(msg)
            #print 'send_val[' + str(i) + '] '+ str(send_vals[i])
        #print arg_buffer
        #send mean
    else:
        for i in xrange(5):
            #print str(args[i]) + ' ---- args[' + str(i) + ']'
            arg_buffer[i] = args[i]
            count += 1

    #for i in xrange(5):
        #print str(args[i]) + ' ---- args[' + str(i) + ']'
    #print str(args[0]) + '--- args[0]'
    #print str(args[1]) + '--- args[1]'



s.addMsgHandler("/muse/eeg",response)

def each_frame():
    # clear timed_out flag
    s.timed_out = False
    # handle all pending requests then return
    while not s.timed_out:
        s.handle_request()





def main():
    """This runs the protocol on port 8000"""

    while run:
    	time.sleep(1)
    	each_frame()
    s.close()
'''
    while True:
    	data,addr = sock.recvfrom(1024)
    	print data + ' IN WHILE LOOP'
'''
	#time.sleep(2)


if __name__ == '__main__':
    main()


'''
for i in xrange(1,10):
	engine = pyttsx.init()
	engine.say('Hello Asshole')
	engine.runAndWait()
	engine.stop()
	print i
	time.sleep(10)
	'''
