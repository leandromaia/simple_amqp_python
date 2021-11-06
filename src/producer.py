#!/usr/bin/env python
import os, sys

import pika

from connection import AMQPConnection


def main():
    broker = AMQPConnection()

    while True:
        message = input("Forneça a sua mensagem:\n->\t")
        broker.emit(message)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Envio de mensagem finalizado!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
