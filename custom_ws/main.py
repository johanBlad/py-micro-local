import signal
import sys

from server import WebServer


def shutdownServer(sig, unused):
    server.shutdown(server.socket)
    sys.exit(1)

signal.signal(signal.SIGINT, shutdownServer)
server = WebServer('localhost', 8010)

server.start()

