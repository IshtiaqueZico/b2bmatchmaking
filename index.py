# Import the required modules
import http.server
import socketserver

# Create a handler for the HTTP server
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
  # Override the do_GET method to serve an HTML page
  def do_GET(self):
    # Set the response code and headers
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    # Write the HTML page to the response
    self.wfile.write(b'<!DOCTYPE html>\n')
    self.wfile.write(b'<html>\n')
    self.wfile.write(b'  <head>\n')
    self.wfile.write(b'    <title>My HTTP Server</title>\n')
    self.wfile.write(b'  </head>\n')
    self.wfile.write(b'  <body>\n')
    self.wfile.write(b'    <h1>Hello, World!</h1>\n')
    self.wfile.write(b'  </body>\n')
    self.wfile.write(b'</html>\n')

# Create an instance of the HTTP server
httpd = socketserver.TCPServer(('', 8000), MyHTTPRequestHandler)

# Start the HTTP server
httpd.serve_forever()
