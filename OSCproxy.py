import OSC
import time
import os
import socket
import numpy as np
import types



UDP_IP = "127.0.0.1"
UDP_PORT = 8200
addr = '127.0.0.1',8200

weki_address = '127.0.0.1', 6448
weki = OSC.OSCClient()
weki.connect(weki_address)

s = OSC.OSCServer(addr)
s.timeout = 0
run = True

count = 0
arg_buffer = np.empty((5, 10))

def handle_timeout(self):
    self.timed_out = True

s.handle_timeout = types.MethodType(handle_timeout, s)

def response(path,tags, args, source):
    global arg_buffer
    global count
    if count >= 10:
        msg = OSC.OSCMessage()
        msg.setAddress("/wek/inputs")
        send_vals = [None] * 5
        count = 0
        for i in xrange(5):
            send_vals[i] = np.mean(arg_buffer[i])
            msg.append(send_vals[i])
        weki.send(msg)

    else:
        for i in xrange(5):
            arg_buffer[i] = args[i]
            count += 1

s.addMsgHandler("/muse/eeg",response)

def each_frame():
    s.timed_out = False
    while not s.timed_out:
        s.handle_request()

def main():

    while run:
    	time.sleep(1)
    	each_frame()
    s.close()

if __name__ == '__main__':
    main()
