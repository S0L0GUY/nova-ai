import json

class history:
    def __init__(self):
        history_path = 'variable/history.json'
    
    def get(self):
        """
        Retrieves the history data from a JSON file.
        Returns:
            dict: The history data loaded from the JSON file.
        """
        
        with open(self.history_path, 'r') as file:
            return json.load(file)
    
    def add(self, entry):
        """
        Adds a new entry to the history.
        Args:
            entry (str): The entry to be added to the history.
        """
        
        current_history = self.get()
        current_history.append(entry)
        self.set(current_history)
    
    def set(self, history):
        """
        Save the given history data to a JSON file.
        Args:
            history (dict): The history data to be saved.
        Writes the history data to 'variable/history.json' with an indentation of 4 spaces.
        """
        
        with open(self.history_path, 'w') as file:
            json.dump(history, file, indent=4)