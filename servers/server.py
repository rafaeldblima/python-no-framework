import json
from http.server import BaseHTTPRequestHandler

from partidos.urls import get_path


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        status_code, response = get_path(
            path=self.path,
            request_type=self.command
        )
        self.respond(status_code, response)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data
        )

        self.respond(status_code, response)

    def do_PUT(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data
        )

        self.respond(status_code, response)

    def do_PATCH(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data
        )

        self.respond(status_code, response)

    def do_DELETE(self):
        status_code, response = get_path(
            path=self.path,
            request_type=self.command
        )
        self.respond(status_code, response)

    def do_OPTIONS(self):
        status_code, response, headers = get_path(
            path=self.path,
            request_type=self.command
        )
        self.respond(status_code, response, headers)

    def handle_http(self, status_code, data, headers=None):
        self.send_response(status_code)
        self.send_header('WWW-Authenticate', 'Basic realm="Rafael Lima"')
        self.send_header('Content-Type', 'application/json')
        if headers:
            self.send_header('Allow', headers)
        self.end_headers()
        content = json.dumps(data)
        return bytes(content, 'UTF-8')

    def respond(self, status_code, data=None, headers=None):
        response = self.handle_http(status_code, data, headers)
        self.wfile.write(response)
