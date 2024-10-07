# from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime
import json
import urllib.parse

# http://192.168.0.19:8080/status
# http://192.168.0.19:8080/add_message/This%20is%20a%20test
# http://192.168.0.19:8080/logs

# TODO: Make sound effect thingy

def add_message(message):
    """
    Args:
        message (string): The message to add to the history.

    Returns:
        string: Success message.

    Add a message as "user" to history.json.
    """    
    with open('history.json', 'r') as file:
        history = json.load(file)

    history.append({"role": "user", "content": message})

    with open('history.json', 'w') as file:
        json.dump(history, file, indent=4)

    return f"Added '{message}' to history."

def mood():
    """
    Returns:
        string: The current mood.

    Look in var/mood.txt and return the value as a string.
    """    
    with open('var/mood.txt', 'r') as file:
        # Get the current mood
        mood = file.read()

    return f"mood: {mood}"

def logs():
    """
    Returns:
        string: The content of history.json as a string.

    Look at history.json, format it as a string, and return it.
    """    
    with open('history.json', 'r') as file:
        loaded_data = json.load(file)
    return json.dumps(loaded_data, indent=4)

def status():
    """
    Returns:
        string: "Server is operational"

    Return a message indicating that the server is online and ready.
    """    
    return "Server is operational"

def remove_leading_space(s):
    """
    Args:
        s (string): The inputted command.

    Returns:
        string: The inputted command without a leading space in front.

    Look to see if there is a space at the front of the command and remove it if there is.
    """    
    if s and s[0] == ' ':
        return s[1:]
    return s

def reset_logs():
    """
    Returns:
        string: Success message.

    Reset the logs in history.json to the original state and return a success message.
    """    

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

    system_prompt = f"{system_prompt} \n {additional_system_prompt}" # Construct the final system prompt

    now = datetime.now()

    history = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": f"Today is {now.strftime("%Y-%m-%d")}"},
        {"role": "user", "content": "Hey"},
        {"role": "assistant", "content": "Hi, im Nova."},
        {"role": "user", "content": "Are you a real person?"},
        {"role": "assistant", "content": "Yea"},
    ]
    
    with open('history.json', 'w') as file:
        json.dump(history, file, indent=4)

    return "Logs Cleared"

# Define a function to handle commands
def handle_command(user_command, *args):
    """
    Args:
        user_command (string): The command to be run.

    Returns:
        string: The outputting message.

    Handle a command and return the output of whatever was run.
    """    
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
    """
    Args:
        server_class (object, optional): The type of server that is being run. Defaults to ThreadingHTTPServer.
        handler_class (object, optional): The type of request handler that is being used. Defaults to RequestHandler.
        port (integer, optional): The port that the server is hosted on. Defaults to 8080.

    Create a web server on port 8080
    """    
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
