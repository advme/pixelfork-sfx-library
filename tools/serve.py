#!/usr/bin/env python3
"""Local preview server with caching switched off.  python3 tools/serve.py 8766"""
import functools, http.server, os, socketserver, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8766
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('', port), functools.partial(Handler, directory=ROOT)) as httpd:
    print('Preview:  http://localhost:{}/tools/preview.html'.format(port))
    print('Demo:     http://localhost:{}/demo/game.html'.format(port))
    print('Ctrl+C to stop.')
    httpd.serve_forever()
