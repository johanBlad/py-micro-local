import socket
import sys

from http_utils import parse_http, make_wsgi_env


class WebServer(object):
    def __init__(self, hostname, port, app):
        self.port = port
        self.host = hostname
        self.application = app

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            print(f"Starting server on {self.host}:{self.port}")
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            print(f"SUCCESS!")
            print("Press Ctrl+C to shut down server.")
        except Exception as e:
            print(f"Error: Could not bind to port {self.port}")
            self.shutdown(self.socket)
            sys.exit(1)

        self.listen()

    def listen(self):
        self.socket.listen(5)
        while True:
            conn, addr = self.socket.accept()
            conn.settimeout(15)
            print(f"Connection received from {addr}")
            self.handle_client(conn, addr)
            # threading.Thread(target=self._handle_client, args=(client, address)).start()

    def handle_client(self, conn, addr):
        def start_response(status, headers):
            conn.sendall(f"HTTP/1.1 {status}\r\n".encode())
            for (key, value) in headers:
                conn.sendall(f"{key}: {value}\r\n".encode())
            conn.sendall("\r\n".encode())

        while True:
            try:
                http_req = conn.recv(1024).decode()
                if not http_req:
                    break

                parsed_req = parse_http(http_req)
                environ = make_wsgi_env(*parsed_req)
                response_body = self.application(environ, start_response)
                for data in response_body:
                    conn.sendall(data.encode())
                conn.sendall("\r\n\r\n".encode())
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                break
            except Exception as e:
                print("ERROR: ", e)
                break

    # def start_response(self, conn, status, headers):
    #     conn.sendall(f"HTTP/1.1 {status}\r\n")
    #     for (key, value) in headers:
    #         conn.sendall(f"{key}: {value}\r\n")
    #     conn.sendall("\r\n ")

    def shutdown(self, s):
        try:
            print("Shutting down server")
            s.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
