import os, http.server, socketserver
os.chdir("/Users/dfa/Desktop/Website")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 3000), handler) as httpd:
    httpd.serve_forever()
