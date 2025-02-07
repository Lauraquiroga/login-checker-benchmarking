from datetime import datetime
import random
import string
import time

class Helper:
    @staticmethod
    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            return result, elapsed_time  # Return both the function result and execution time
        return wrapper


    @staticmethod
    def load_usernames(file_path):
        """
        Reads usernames from a text file and returns them as a list.

        Parameters:
        file_path (str): The path to the dataset file.

        Returns:
        list: A list of usernames.
        """
        with open(file_path, 'r') as file:
            return file.read().splitlines()
        
    @staticmethod
    def create_new_dataset(size, word_length=10):
        usernames = Helper.generate_usernames(size, word_length)
        Helper.save_usernames(usernames)
        
    @staticmethod
    def save_usernames(data):
        """
        Saves the list of usernames to a text file with a timestamp suffix in the filename.

        Parameters:
        data (list): A list of usernames to be saved.

        File format:
        The file will be saved in the './data/' directory with a filename that includes a timestamp
        (format: YYYYMMDD_HHMMSS). Each username in the list will be written to a new line in the file.

        Example:
        If 'data' = ['user1', 'user2'], the file will contain:
        user1
        user2

        The file will be saved with a name like 'usernames_20250203_123456.txt'
        """
        # Generate the current timestamp in the format: YYYYMMDD_HHMMSS
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Open the file with the generated filename and write the usernames to it
        with open(f'./data/usernames_{timestamp}.txt', 'w') as file:
            file.write('\n'.join(data))

    
    @staticmethod
    def generate_usernames(dataset_size, length=10):
        """
        Generate the dataset using random usernames (including letters and digits)

        Parameters:
        dataset_size (int): The size of the dataset
        length (int): Length of each randomly generated username

        Returns:
        list of str: a list containing all usernames
        """
        return [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(dataset_size)]