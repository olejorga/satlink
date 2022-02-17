from http.server import BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.wfile.write()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.wfile.write()