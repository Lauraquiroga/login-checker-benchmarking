from src.utils import Helper

class LoginChecker:

    def __init__(self, usernames):
        self.data = usernames

    def main():
        # Load dataset
        file_path = './data/usernames.txt'
        usernames_data = Helper.load_usernames(file_path)
        #Helper.save_usernames(["testing","names"])
        LoginChecker(usernames_data)
    
    if __name__ == '__main__':
        main()