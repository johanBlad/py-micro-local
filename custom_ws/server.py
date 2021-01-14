import socket
import sys

from http_utils import parse_http, make_http_response


class WebServer(object):
    def __init__(self, hostname, port):
        self.port = port
        self.host = hostname

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

        while True:
            try:
                http_req = conn.recv(1024).decode()
                if not http_req:
                    break

                parsed_req = parse_http(http_req)
                res = "Hello from custom webserver\n"
                http_res = make_http_response(res)
                conn.sendall(http_res.encode("utf-8"))
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                break
            except Exception as e:
                print("ERROR: ", e)
                break

    def shutdown(self, s):
        try:
            print("Shutting down server")
            s.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass


# /*
# with socket.socket() as s:
#     print('binding!')
#     s.bind(('localhost', 8020))
#     s.listen(1)
#     conn, addr = s.accept()
#     print('pre loop')
#     while True:

#         print('conn', conn)
#         with conn:
#             try:
#                 http_req = conn.recv(1024).decode('utf-8')
#                 parsed_req = parse_http(http_req)
#                 res = 'Hello from custom webserver\n'
#                 http_res = make_http_response(res)
#                 conn.sendall(http_res.encode('utf-8'))
#             except OSError as err:
#                 print('catch!')
#                 print(err)

