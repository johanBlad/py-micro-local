import signal
import sys

from server import WebServer
from wsgi import application


def shutdownServer(sig, unused):
    server.shutdown(server.socket)
    sys.exit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdownServer)
    server = WebServer("localhost", 8001, application)
    server.start()

