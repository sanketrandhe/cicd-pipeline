from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Day 14 CI/CD Pipeline!")

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Application running on port 5000")

server.serve_forever()













