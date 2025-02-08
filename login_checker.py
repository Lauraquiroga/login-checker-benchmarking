from src.utils import Helper
from src.benchmark import Benchmark

class LoginChecker:

    def __init__(self, usernames):
        b = Benchmark(usernames)
        b.run_simulation()
        Helper.save_results(b.results, b.dataset_sizes)
        b.show_plot_comparison()
    

def main():
    # Load dataset
    file_path = './data/usernames_1M.txt'
    usernames_data = Helper.load_usernames(file_path)

    LoginChecker(usernames_data)


if __name__ == '__main__':
    main()