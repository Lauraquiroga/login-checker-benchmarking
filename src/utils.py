from datetime import datetime
import random
import string
import time
import json

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
    
    @staticmethod
    def save_results(exec_times, data_sizes):
        """
        Saves the results of the simulation into a JSON file with a unique filename.

        The filename is generated dynamically using:
        - The final dataset size analyzed
        - The number of steps in between data sizes
        - A timestamp for uniqueness

        Format:
        {
            "Exec_times": { "Linear": [], "Binary": [], "Hashing": [], "Bloom": [], "Cuckoo": [] },
            "Data_sizes": []
        }

        Parameters:
        exec_times (dict): The results of the simulation, in the format:
                        { "Linear": [], "Binary": [], "Hashing": [], "Bloom": [], "Cuckoo": [] }
        data_sizes (list of int): The dataset sizes that correspond to the execution times.

        Returns:
        bool: True if the file is saved successfully, False otherwise.
        """
        try:
            final_size = data_sizes[-1] if data_sizes else "unknown"
            num_steps = len(data_sizes)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"data/results/benchmark_results_{final_size}_steps{num_steps}_{timestamp}.json"

            results = {
            "Exec_times": exec_times,
            "Data_sizes": data_sizes
            }

            with open(filename, "w") as file:
                json.dump(results, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False
        
    @staticmethod
    def read_results_from_json(filename):
        """
        Read the JSON file and store its content in 'results'.
        The structure of the json file is as follows:
        {
            "Exec_times": { "Linear": [], "Binary": [], "Hashing": [], "Bloom": [], "Cuckoo": [] },
            "Data_sizes": []
        }

        """
        # 
        with open(filename, 'r') as file:
            results = json.load(file)

        return results