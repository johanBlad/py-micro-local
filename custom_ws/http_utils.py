from io import StringIO


def parse_http(http):
    request, *headers, _, body = http.split("\r\n")
    method, path, protocol = request.split(" ")
    headers = dict(attr.split(":", maxsplit=1) for attr in headers)
    return method, path, protocol, headers, body


def encode_response(response, response_type):
    if response_type == "text/html":
        response = bytes(response + "\r\n", "utf-8")
    return response


def make_wsgi_env(method, path, protocol, headers, body):
    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "SERVER_PROTOCOL": protocol,
        "wsgi.input": StringIO(body),
    }
    environ.update({f"HTTP_{key.upper()}": value for (key, value) in headers.items()})
    return environ
