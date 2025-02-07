from src.utils import Helper
from src.benchmark import Benchmark

class LoginChecker:

    def __init__(self, usernames):
        b = Benchmark(usernames)
        b.run_simulation()
    

def main():
    # Load dataset
    file_path = './data/usernames_10M.txt'
    usernames_data = Helper.load_usernames(file_path)

    #LoginChecker(usernames_data)
    #Helper.create_new_dataset(10000000)


if __name__ == '__main__':
    main()