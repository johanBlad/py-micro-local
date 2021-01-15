import signal
import sys

from server import WebServer


def view(path):
    response = f"Hello custom webserver from {path}"
    response_type = "text/html"
    status = str(200) + " OK"
    if response_type == "text/html":
        response += "\r\n"
    headers = [("Content-Length", str(len(response))), ("Content-Type:", response_type)]
    return status, headers, response


def application(environ, start_response):
    path = environ["PATH_INFO"]
    status, headers, response = view(
        path
    )  # Dynamic content specified by app, generated from the request info
    start_response(status, headers)
    return [response]


def shutdownServer(sig, unused):
    server.shutdown(server.socket)
    sys.exit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdownServer)
    server = WebServer("localhost", 8010, application)
    server.start()

