from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello from Python app deployed via Cloud Build!')

if __name__ == '__main__':
    server = HTTPServer(('', 8080), SimpleHandler)
    print('Server running on port 8080...')
    server.serve_forever()
