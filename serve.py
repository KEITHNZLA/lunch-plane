import http.server
import socketserver

PORT = 3000
DIRECTORY = "/Users/keithfitzsimons/Documents/Lunch P/.claude/worktrees/zen-zhukovsky-53808a"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
