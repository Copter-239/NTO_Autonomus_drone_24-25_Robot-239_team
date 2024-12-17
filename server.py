from http.server import BaseHTTPRequestHandler, HTTPServer

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request, Path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open('site.html', 'r').read().encode('utf-8'))
        elif self.path.endswith("/get/start") or self.path.endswith("/get/stop") or self.path.endswith("/get/kill") or self.path.endswith("/get/update"):
            if self.path.endswith("/get/start"):
                print(1)
            if self.path.endswith("/get/stop"):
                print(2)
            if self.path.endswith("/get/kill"):
                print(3)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<meta http-equiv="refresh" content="0;url=/">'.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':

    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)


#http://localhost:8000/




