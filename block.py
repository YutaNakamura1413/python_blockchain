import hashlib
import time
import json

class Block:
    def __init__(self, index, difficulty, time, prev_block, tx):
        self.index = index
        self.difficulty = difficulty
        self.time = time
        self.prev_block = prev_block
        self.tx = tx
        self.nonce = None
        self.current_block = None

    def seek_hash(self, nonce):
        data = {
            "index": self.index,
            "difficulty": self.difficulty,
            "time": self.time,
            "prev_block": self.prev_block,
            "tx": self.tx,
            "nonce": nonce
        }
        hash1 = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
        hash2 = hashlib.sha256(hash1.encode()).hexdigest()
        return(hash2)

    def mining(self):
        nonce = 0
        while True:
            hash = self.seek_hash(nonce)
            if (hash[:self.difficulty] == "0" * self.difficulty):  # nonceが見つかった場合
                self.nonce = nonce
                self.current_block = hash
                # print("index:", self.index)
                # print("difficulty:", self.difficulty)
                # print("time:", self.time)
                # print("nonce:", self.nonce)
                # print("hash:", self.current_block)
                # print("////////////////////////")
                break
            else:
                nonce += 1

    def add_nonce(self, nonce):
        self.nonce = nonce

    def send_block(self):
        data = {
            "index": self.index,
            "difficulty": self.difficulty,
            "time": self.time,
            "prev_block": self.prev_block,
            "tx": self.tx,
            "nonce": self.nonce,
            # "cuurent_block": self.current_block
        }
        return json.dumps(data)