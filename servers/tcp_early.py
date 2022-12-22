import socket
import struct

# localIP     = "127.0.0.1"
# localIP     = "10.105.86.160"
localIP     = ""
localPort   = 8000
bufferSize  = 1024
bfr = []
msgFromServer       = "Hello TCP Client"
bytesToSend         = str.encode(msgFromServer)
max_temp = float('-inf')
min_temp = float('inf')
cnt = 0
hum_arr = []

# Create a datagram socket
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Bind to address and ip
s.bind((localIP, localPort))
s.listen()
print("TCP server up and listening")
def hex_str_to_float(s1):
    s2 = ['0']*8
    s2[0] = s1[6]
    s2[1] = s1[7]
    s2[2] = s1[4]
    s2[3] = s1[5]
    s2[4] = s1[2]
    s2[5] = s1[3]
    s2[6] = s1[0]
    s2[7] = s1[1]
    s2 = "".join(s2)
    f = struct.unpack('!f', bytes.fromhex(s2))[0]
    return f
def int_str_to_float(s1):
    s2 = ['0']*8
    s2[0] = s1[6]
    s2[1] = s1[7]
    s2[2] = s1[4]
    s2[3] = s1[5]
    s2[4] = s1[2]
    s2[5] = s1[3]
    s2[6] = s1[0]
    s2[7] = s1[1]
    s2 = "".join(s2)
    f = struct.unpack('!I', bytes.fromhex(s2))[0]
    return f
# Listen for incoming connections
fl = open('data.txt', 'a')
while(True):
    conn, addr = s.accept()
    msg = conn.recv(bufferSize)

    if msg:
        cnt += 1
        #fl.write(str(message))
        temp = hex_str_to_float(msg.decode()[:8])
        hum = hex_str_to_float(msg.decode()[8:16])
        hum_arr.append(hum)
        if(len(hum_arr) > 4):
            hum_arr.pop(0)
        count = int_str_to_float(msg.decode()[16:24])
        print("temp: " + str(temp)) 
        print("hum: " + str(hum)) 
        print("message id: " + str(count) + " server id: " + str(cnt))
        fl.write(str(temp) + "," + str(hum) + "," + str(count)+"\n")

# Sending a reply to client
# UDPServerSocket.sendto(bytesToSend, address)
