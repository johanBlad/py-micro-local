from io import StringIO


def parse_http(http):
    request, *headers, _, body = http.split("\r\n")
    method, path, protocol = request.split(" ")
    headers = dict(attr.split(":", maxsplit=1) for attr in headers)
    return method, path, protocol, headers, body


def make_http_response(res):
    return (
        "HTTP/1.1 200 OK \r\n"
        + f"Content-Length: {len(res)}\r\n"
        + "Content-Type: text/html"
        + "\r\n"
        + "\r\n"
        + res
        + "\r\n"
    )


def make_wsgi_env(method, path, protocol, headers, body):
    environ = {
        "REQUEST_METHOD": method,
        "PATH_INFO": path,
        "SERVER_PROTOCOL": protocol,
        "wsgi.input": StringIO(body),
    }
    environ.update({f"HTTP_{key.upper()}": value for (key, value) in headers.items()})
    return environ
