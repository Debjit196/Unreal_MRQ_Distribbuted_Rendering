
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import sys
import os
import json
sys.path.append(os.getcwd())
import client_launch
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        if(self.headers.get('content-length')!=None):
            length = int(self.headers.get('content-length'))
            payload_string = self.rfile.read(length).decode('utf-8')
            payload = json.loads(payload_string) if payload_string else None
            print("The header is ",payload)
            
            print("It is ready vfor launch")
            client_launch.launcher(data=payload)
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=None):
    import socket   
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname)   
    logging.basicConfig(level=logging.INFO)
    server_address = (IPAddr, port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
