import matplolib.pyplot as plt

class Benchmark:
    """
    """
    def __init__(self):
        self.colour_key = {'Linear':'cornflowerblue', 'Binary':'darkorange', 'Hashing':'red', 'Bloom':'green', 'Cuckoo': 'purple'}

    def show_plot_comparison():
        fig = plt.figure()
        
        plt.ylabel('Run time (s)')
        plt.xlabel('Size of the dataset')
        plt.title(f"Comparison of Run Time Complexity")
        plt.legend()