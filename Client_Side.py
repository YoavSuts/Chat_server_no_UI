import socket
import threading
from time import sleep
import sys

import ChatGui
from ChatGui import *

MAX_MSG_LENGTH = 1024
ChatGui.start()

def recv_Message(s, stop):
    while True:
        data = s.recv(MAX_MSG_LENGTH).decode()
        print(f"\n{data}\nEnter message: ", end=' ')
        if stop is True:
            break


def open_sock_and_send_messages():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 5555))
        stop = False
        is_enter_message = True
        x = threading.Thread(target=recv_Message, daemon=True, args=(s, lambda: stop))
        x.start()
        while True:
            if is_enter_message is True:
                message = input("Enter message: ")
            else:
                is_enter_message = True
                message = input()
            if message == "STOP":
                break
            try:
                if message[0] == "@":
                    is_enter_message = False
            except IndexError:
                print("please enter a valid message")
            s.send(message.encode('UTF-8'))
            sleep(1)
    s.send(message.encode('UTF-8'))
    stop = True
    x.join()

open_sock_and_send_messages()
