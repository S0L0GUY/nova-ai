from commands.mood import Mood

mood = Mood()
import os

class prompt:
    def __init__(self):
        pass
    
    def get_all_prompt_paths(self):
        """
        Retrieves all prompt file paths from the specified directory.
        This method scans the 'text_files/prompts' directory for files with a '.txt' extension.
        It categorizes these files based on the prefix before the first underscore in the filename.
        The resulting dictionary maps each mood (prefix) to the corresponding file path.
        Returns:
            dict: A dictionary where keys are moods (str) and values are file paths (str).
        """
        directory = 'text_files/prompts'
        mood_prompts = {}

        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                mood = filename.split('_')[0]
                mood_prompts[mood] = os.path.join(directory, filename)
        
        return mood_prompts
    
    def get_mood_path(self, mood):
        """
        Retrieve the file path associated with a given mood.
        Args:
            mood (str): The mood for which to retrieve the file path.
        Returns:
            str: The file path associated with the specified mood.
        """
        
        return self.get_all_prompt_paths()[mood]
    
    def get_system_prompt(self):
        """
        Generates a system prompt based on the current mood and an additional prompt.
        This function retrieves the current mood, reads the corresponding mood prompt
        from a file, and appends an additional prompt to it.
        Returns:
            str: The combined system prompt consisting of the mood prompt and the additional prompt.
        """
        
        current_mood = mood.get()
        mood_path = self.get_mood_path(current_mood)
        
        with open(mood_path, 'r') as file:
            mood_prompt = file.read()
        
        additional_path = self.get_mood_path('additional')
        
        with open(additional_path, 'r') as file:
            additional_prompt = file.read()
        
        return f"{mood_prompt}\n{additional_prompt}"