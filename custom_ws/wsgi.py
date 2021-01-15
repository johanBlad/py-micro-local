from app import view


def application(environ, start_response):
    path = environ["PATH_INFO"]
    status, headers, response = view(
        path
    )  # Dynamic content specified by app, generated from the request info
    start_response(status, headers)
    return [response]
