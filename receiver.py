import threading # See https://docs.python.jp/3/library/threading.html
import socket    # See https://docs.python.jp/3/library/socket.html
import json
import setting
from block import Block

BUFFER_SIZE = 1024
class Receiver(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self, name="receiver")
        self.host = host
        self.port = port
        # self.blocks = []

    def run(self):
        # Listen
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # SOCK_STREAM: TCP, SOCK_DGRAM: UDP
            sock.bind((self.host, self.port))
            sock.listen(10)
            while True:
                (conn, addr) = sock.accept()
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if data:
                        data_dict = json.loads(data)
                        # print(data_dict)
                        new_block = Block(data_dict["index"], data_dict["difficulty"],
                                         data_dict["time"], data_dict["prev_block"],
                                         data_dict["tx"])
                        new_block.add_nonce(data_dict["nonce"])
                        setting.chain.append_block(new_block)
                        # print("newblock prevHash", new_block.prev_block)

                    else:
                        break
