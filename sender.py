import threading # See https://docs.python.jp/3/library/threading.html
import socket    # See https://docs.python.jp/3/library/socket.html
import time
import setting
from block import Block

BUFFER_SIZE = 1024
class Sender(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self, name="sender")
        self.host = host
        self.port = port
        # self.blocks = []

    def run(self):
        index = 0
        difficulty = 5
        genesis_time = "00000000"
        prev_block = "0000000000000000000000000000000000000000000000000000000000000000"
        tx = "txtxtx"

        genesis_block = Block(index, difficulty, genesis_time, prev_block, tx)
        genesis_block.mining()
        setting.chain.append_genesisblock(genesis_block)

        prev_block = genesis_block.current_block

        # print(self.blocks)
        msg = input("> ")
        while True:

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # SOCK_STREAM: TCP, SOCK_DGRAM: UDP
                sock.connect((self.host, self.port))
                # sock.sendall(msg.encode("utf-8"))

                new_block = Block(setting.chain.block_chain[len(setting.chain.block_chain)-1].index + 1,
                                  difficulty,
                                  time.time(),
                                  setting.chain.block_chain[len(setting.chain.block_chain)-1].current_block,
                                  tx)
                new_block.mining()
                data = new_block.send_block()
                sock.sendall(data.encode("utf-8"))

                # result = sock.recv(BUFFER_SIZE)
                # print('receive', result)

                # self.blocks.append(new_block)
                setting.chain.append_block(new_block)
                index += 1
                # prev_block = new_block.current_block

        sock.shutdown(2)
        sock.close()