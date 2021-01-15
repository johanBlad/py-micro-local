from http_utils import encode_response


def view(path):
    response_type = "text/html"
    response = encode_response(f"Hello custom webserver from {path}", response_type)

    status = str(200) + " OK"
    headers = [("Content-Length", str(len(response))), ("Content-Type", response_type)]
    return status, headers, response
