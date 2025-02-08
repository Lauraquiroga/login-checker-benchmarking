from src.utils import Helper
from src.benchmark import Benchmark

class LoginChecker:
    """
    Class responsible for checking login simulations using a benchmark tool.

    This class runs a benchmark simulation over a list of usernames and saves the results.
    It uses the Benchmark class to simulate login checks, visualize the comparison of results, 
    and store the simulation outcomes using Helper methods.
    """

    def __init__(self, usernames):
        """
        Initializes the LoginChecker class and runs a benchmark simulation.

        The initialization process involves creating a Benchmark instance, running the simulation, 
        saving the results, and showing the plot comparison.

        Parameters:
        usernames (list of str): List of usernames to run the benchmark on.
        """
        b = Benchmark(usernames, n_steps=10)
        b.run_simulation()
        Helper.save_results(b.results, b.dataset_sizes)
        b.show_plot_comparison()
    

def main():
    """
    Main function to load the dataset and initiate the login check simulation.

    This function loads the usernames from a file and passes them to the LoginChecker 
    to perform the benchmark simulation.
    """
    # Load dataset
    file_path = './data/usernames_1M.txt'
    usernames_data = Helper.load_usernames(file_path)

    LoginChecker(usernames_data)

if __name__ == '__main__':
    main()