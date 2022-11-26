import sys

from gevent.pywsgi import WSGIServer
from app import create_app

try:
    port = int(sys.argv[1] if len(sys.argv) > 1 else 5001)
    host = sys.argv[2] if len(sys.argv) > 2 else '0.0.0.0'
    print('[*] Starting server on {}:{}'.format(host, port))

    http_server = WSGIServer((host, port), create_app())
    http_server.serve_forever()
except KeyboardInterrupt:
    print('[+] Server closed')
