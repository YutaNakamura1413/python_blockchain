import threading # See https://docs.python.jp/3/library/threading.html
import socket    # See https://docs.python.jp/3/library/socket.html

import setting
from receiver import Receiver
from sender import Sender


def main():
    setting.init()
    host     = input("Your IP or hostname: ")
    port     = int(input("Your port: "))
    receiver = Receiver(host, port)

    partner_host = input("Partner's IP or hostname: ")
    partner_port = int(input("Partner's port: "))
    sender       = Sender(partner_host, partner_port)

    threads = [receiver.start(), sender.start()]

if __name__ == '__main__':
    main()
