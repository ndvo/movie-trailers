import re
import BaseHTTPServer


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """ Handles the HTTP requests.
    Returns not found unless explicitly created routes are found."""

    routes = {}

    def do_GET(self):
        result = False
        for k, v in self.routes.iteritems():
            if re.match(k, self.path):
                result = v()
        if result:
            self.send_response(200)
            if result.header:
                for k, v in result.header.iteritems():
                    self.send_header(k, v)
            else:
                self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(result.body)
        else:
            self.send_response(404)
