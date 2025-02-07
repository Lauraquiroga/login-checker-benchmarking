from src.utils import Helper
from src.benchmark import Benchmark

class LoginChecker:

    def __init__(self, usernames):
        b = Benchmark(usernames)
        b.run_simulation()
        Helper.save_results(b.results, b.dataset_sizes)
        #results = Helper.read_results_from_json('data/results/benchmark_results_1000000_steps100_20250207-134453.json')
        #b.show_plot_comparison_from_results(results)
        b.show_plot_comparison()
    

def main():
    # Load dataset
    file_path = './data/usernames_1M.txt'
    usernames_data = Helper.load_usernames(file_path)

    LoginChecker(usernames_data)
    #Helper.create_new_dataset(10000000)



if __name__ == '__main__':
    main()