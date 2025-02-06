from src.utils import Helper
from src.linear_search import LinearSearch
from src.bloom_filter import BloomFilter

class LoginChecker:

    def __init__(self, usernames):
        self.data = usernames
        linear = LinearSearch(self.data)
        print(linear.exists('testing'))
        bloom = BloomFilter(len(self.data), fp_prob=0.01)
        bloom.initialize_with_dataset(self.data)
        print(bloom.exists('testing'))


def main():
    # Load dataset
    file_path = './data/usernames_1M.txt'
    usernames_data = Helper.load_usernames(file_path)
    #Helper.save_usernames(["testing","names"])
    LoginChecker(usernames_data)

if __name__ == '__main__':
    main()