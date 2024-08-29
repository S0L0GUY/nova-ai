from http.server import BaseHTTPRequestHandler, HTTPServer
from pythonosc import udp_client

class OSCRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract the message from the URL query
        path = self.path.split("?")
        if len(path) > 1:
            params = path[1].split("=")
            if len(params) == 2 and params[0] == "message":
                message = params[1]

                # Set up the OSC client to send to the specified IP and port
                client = udp_client.SimpleUDPClient("192.168.0.19", 9000)
                client.send_message("/chatbox/input", message)

                # Send a success response to the browser
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"OSC command sent successfully!")
                return

        # Send an error response if the message is missing
        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Missing message!")

def run(server_class=HTTPServer, handler_class=OSCRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
