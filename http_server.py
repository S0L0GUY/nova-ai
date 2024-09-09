from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse

# http://192.168.0.19:8080/status
# http://192.168.0.19:8080/add_message/This%20is%20a%20test
# http://192.168.0.19:8080/logs


def add_message(message):
    with open('history.json', 'r') as file:
        history = json.load(file)

    history.append({"role": "user", "content": message})

    with open('history.json', 'w') as file:
        json.dump(history, file, indent=4)

    return f"Added '{message}' to history."

def mood():
    with open('var/mood.txt', 'r') as file:
        # Get the current mood
        mood = file.read()

    return f"mood: {mood}"

def logs():
    with open('history.json', 'r') as file:
        loaded_data = json.load(file)
    return json.dumps(loaded_data, indent=4)

def status():
    return "Server is operational"

def remove_leading_space(s):
    if s and s[0] == ' ':
        return s[1:]
    return s

# Define a function to handle commands
def handle_command(user_command, *args):
    command = remove_leading_space(user_command)

    if command == "add_message":
        return add_message(" ".join(args))
    elif command == "logs":
        return logs()
    elif command == "status":
        return status()
    elif command == "mood":
        return mood()
    else:
        return "Command Not Found."

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_GET(self):
        path = self.path[1:]  # Remove the leading '/'
        parsed_path = urllib.parse.unquote(path)  # Decode URL encoding
        command_parts = parsed_path.split('/')
        command = command_parts[0]
        args = command_parts[1:]

        try:
            result = handle_command(command, *args)
            self._send_response(result)
        except Exception as e:
            self._send_response(f"Error: {str(e)}")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
