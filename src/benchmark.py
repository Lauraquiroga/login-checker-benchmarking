from .linear_search import LinearSearch
from .binary_search import BinarySearch
from .hashing import Hashing
from .bloom_filter import BloomFilter
from .cuckoo_filter import CuckooFilter

from .utils import Helper

import statistics
import matplotlib.pyplot as plt

class Benchmark:
    """
    Benchmarking different search algorithms by varying search space size.
    """

    def __init__(self, dataset):
        """
        Initializes the Benchmark class with the dataset and prepares the necessary attributes.

        Parameters:
        dataset (list): A list containing the full dataset of usernames to be used in benchmarking.
        """
        self.dataset = dataset
        self.random_usernames = Helper.generate_usernames(10)
        self.results = { 'Linear': [], 'Binary': [], 'Hashing': [], 'Bloom': [], 'Cuckoo': [] }
        self.colour_key = {
            'Linear': 'cornflowerblue',
            'Binary': 'darkorange',
            'Hashing': 'red',
            'Bloom': 'green',
            'Cuckoo': 'purple'
        }
        self.dataset_sizes = []  # Tracking dataset sizes

    def run_simulation(self):
        """
        Executes the benchmark by testing each search algorithm over increasing dataset sizes.

        The dataset size starts at 1,000 and increases in steps of 1,000 up to 10 million.
        Each search algorithm is tested on every dataset size, and their execution times are recorded.

        Return:
        dict: A dictionary containing the average execution times for each algorithm across different dataset sizes.
        """
        data_size = len(self.dataset)
        n_steps = 10000 #10k
        step_size = data_size//n_steps
        
        for i in range(n_steps):
            length = (i+1) * step_size
            search_space = self.dataset[:length]

            linear = LinearSearch(search_space)
            self.results['Binary'].append(self.test_algorithm(linear))

            binary = BinarySearch(search_space)
            self.results['Binary'].append(self.test_algorithm(binary))

            hashing = Hashing(search_space)
            self.results['Hashing'].append(self.test_algorithm(hashing))

            bloom = BloomFilter(length)
            bloom.initialize_with_dataset(search_space)
            self.results['Bloom'].append(self.test_algorithm(bloom))

            cuckoo = CuckooFilter(length)
            cuckoo.initialize_with_dataset(search_space)
            self.results['Cuckoo'].append(self.test_algorithm(cuckoo))

        return self.results

    def test_algorithm(self, alg):
        """
        Measures the execution time of the `exists` method for a given search algorithm.

        Each algorithm is tested using a predefined list of randomly generated usernames. 
        The time taken to check for each username is recorded, and the average runtime is computed.

        Parameters:
        alg (object): An instance of a search algorithm class that implements the `exists` method.

        Return:
        float: The average execution time (in seconds) for checking a username in the given search algorithm.
        """
        results =[]
        for username in self.random_usernames:
            _, time_elapsed = alg.exists(username)
            results.append(time_elapsed)
        return statistics.mean(results)

    def show_plot_comparison(self):
        """
        Generates and displays a comparison plot of execution times for each search algorithm.

        The x-axis represents the dataset size, and the y-axis represents the average execution time.
        Each algorithm is represented by a different color.

        The results are retrieved from the `self.results` dictionary.

        Return:
        None
        """
        fig = plt.figure()

        plt.ylabel('Run time (s)')
        plt.xlabel('Size of the dataset')
        plt.title(f"Comparison of Run Time Complexity")

        # Plot each algorithm's results
        for alg, times in self.results.items():
            plt.plot(self.dataset_sizes, times, label=alg, color=self.colour_key[alg])

        plt.legend()
        plt.show()