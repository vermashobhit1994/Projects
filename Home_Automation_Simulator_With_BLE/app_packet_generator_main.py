import socket
import json
import app_packet_generator
import sys
sys.path.append('/home/sobhit/Desktop/ankit_python/home_automation')
from  configuration  import configure as config
Host = config.database['host']
Port = config.database['TCP_PORT_1']


BUFFER_SIZE = config.database['BUFFER_SIZE']
class My_Socket:
   
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect_to_socket(self,host,port):
        self.sock.connect((host,port))

    def send_to_socket(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg)
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + len(msg)

    def receive_from_socket(self):
        byte_string_receive_from_module_C = self.sock.recv(BUFFER_SIZE)
        if byte_string_receive_from_module_C == b'':
            raise RuntimeError("socket connection broken")
        return byte_string_receive_from_module_C

socket_object_c1 = My_Socket()
socket_object_c1.connect_to_socket(Host,Port)
app_packet_generator.packet_init()
while True:
    dict_poacket_1 = app_packet_generator.send_packet_1()
    bytes_string_recv = json.dumps(dict_poacket_1).encode('utf-8') 
    socket_object_c1.send_to_socket(bytes_string_recv)
    connection_id.close()
    socket_object_c2.close()
    socket_object_s1.close()