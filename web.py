from http.server import HTTPServer, BaseHTTPRequestHandler

# Define the HTML content to be served
content = '''
<!DOCTYPE html>
<html>
    <head><title>Hello</title></head>
    <body><h1>Hello</h1></body>
</html>
'''

# Define the request handler
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):  # Correct method name is 'do_GET' not 'do GET'
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Correct header key
        self.end_headers()
        self.wfile.write(content.encode())

# Start the server
print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()  # Correct method is 'serve_forever'
