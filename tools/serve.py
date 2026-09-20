#!/usr/bin/env python3
"""Local preview server with caching switched off.  python3 tools/serve.py 8766

Threaded on purpose.  A single-threaded server deadlocks the whole board:
browsers open speculative connections and send nothing on them, and one idle
socket blocks every other request until it times out.

Range requests are handled too, so <audio> can stream the music files.  Safari
will not start playback on a server that answers a Range request with a 200.
"""
import functools, http.server, os, re, socketserver, sys


class Handler(http.server.SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    timeout = 60                          # drop idle keep-alive sockets

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Accept-Ranges', 'bytes')
        super().end_headers()

    def send_head(self):
        """Serve a byte range when one is asked for, otherwise the whole file."""
        rng = self.headers.get('Range')
        if not rng:
            return super().send_head()

        m = re.match(r'bytes=(\d*)-(\d*)$', rng.strip())
        path = self.translate_path(self.path)
        if not m or not os.path.isfile(path):
            return super().send_head()

        size = os.path.getsize(path)
        first, last = m.group(1), m.group(2)
        if first == '':                       # bytes=-N -> the last N bytes
            if last == '':
                return super().send_head()
            start, end = max(0, size - int(last)), size - 1
        else:
            start = int(first)
            end = int(last) if last else size - 1
        end = min(end, size - 1)

        if start > end or start >= size:
            self.send_response(416)
            self.send_header('Content-Range', 'bytes */%d' % size)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return None

        f = open(path, 'rb')
        f.seek(start)
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Content-Range', 'bytes %d-%d/%d' % (start, end, size))
        self.send_header('Content-Length', str(end - start + 1))
        self.end_headers()
        return _Slice(f, end - start + 1)


class _Slice:
    """File wrapper that stops after `remaining` bytes, for copyfile()."""

    def __init__(self, f, remaining):
        self.f, self.remaining = f, remaining

    def read(self, n=-1):
        if self.remaining <= 0:
            return b''
        if n is None or n < 0:
            n = self.remaining
        chunk = self.f.read(min(n, self.remaining))
        self.remaining -= len(chunk)
        return chunk

    def close(self):
        self.f.close()


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True                     # never hold up Ctrl+C

    def handle_error(self, request, client_address):
        """Browsers abort media requests constantly; that is not an error."""
        if not isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError,
                                              TimeoutError, OSError)):
            super().handle_error(request, client_address)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8766

with Server(('', port), functools.partial(Handler, directory=ROOT)) as httpd:
    print('Preview:  http://localhost:{}/tools/preview.html'.format(port))
    print('Demo:     http://localhost:{}/demo/game.html'.format(port))
    print('Ctrl+C to stop.')
    httpd.serve_forever()
