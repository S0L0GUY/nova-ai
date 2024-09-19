# from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import urllib.parse

# http://192.168.0.19:8080/status
# http://192.168.0.19:8080/add_message/This%20is%20a%20test
# http://192.168.0.19:8080/logs

# TODO: Make sound effect thingy
# TODO: Find out why http requests are slow sometimes

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

def reset_logs():

    mood_prompts = {
        "normal": 'text_files/prompts/normal_system_prompt.txt',
        "argument": 'text_files/prompts/argument_system_prompt.txt',
        "misinformation": 'text_files/prompts/misinformation_system_prompt.txt',
        "drunk": 'text_files/prompts/drunk_system_prompt.txt',
        "depressed": 'text_files/prompts/depressed_system_prompt.txt',
        "therapy": 'text_files/prompts/therapy_system_prompt.txt',
        "anxious": 'text_files/prompts/anxious_system_prompt.txt',
        "sarcasm": 'text_files/prompts/sarcasm_system_prompt.txt',
        "pleasing": 'text_files/prompts/pleasing_system_prompt.txt'
    }

    system_prompt_file = mood_prompts.get(mood, 'text_files/prompts/normal_system_prompt.txt')

    with open(system_prompt_file, 'r') as file:
        system_prompt = file.read()

    with open('text_files/prompts/additional_system_prompt.txt', 'r') as file:
        # Load additional system prompt
        additional_system_prompt = file.read()                      

    system_prompt = f"{system_prompt} \n {additional_system_prompt}"

    history = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Hello, can you introduce yourself to me?"},
    ]
    
    with open('history.json', 'w') as file:
        json.dump(history, file, indent=4)

    return "Logs Cleared"

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
    elif command == "restart":
        return reset_logs()
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


# server_class=HTTPServer, handler_class=RequestHandler, port=8080

def run(server_class=ThreadingHTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
