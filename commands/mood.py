class mood:
    def get():
        """
        Reads the mood from a file and returns it.
        Returns:
            str: The mood read from the file.
        """

        with open('var/mood.txt', 'r') as file:
            mood = file.read()
            return mood

    def set(mood):
        """
        Sets the mood by writing it to a file.
        Args:
            mood (str): The mood to be written to the file.
        Writes the given mood to 'variable/mood.txt'.
        """

        with open('variable/mood.txt', 'w') as file:
            file.write(mood)