# The Login Checker Problem
**Advanced Algorithms (COSC 520) - Assignment 1**     
Author: Laura Quiroga (lquiroga)     

This project implements five algorithms—linear search, binary search, hashing, Bloom filter, and Cuckoo filter—to solve the Login Checker Problem. It also includes a numerical comparison of their performance in terms of time complexity.     

## Project Structure
📂 project_root/     
│── 📂 assets/       
│&emsp;&emsp;│── COSC 520 -Assignment 1.pdf  <-- The assignment instructions      
│      
│── 📂 data/     
│&emsp;&emsp;│── usernames_1M.txt  <-- Dataset file used to perform the runtime complexity analysis     
│&emsp;&emsp;│── 📂 results/  <-- Folder where results are stored after executing the program     
│        
│── 📂 plots/  <-- Plots showing sample results           
│        
│── 📂 src/   
│&emsp;&emsp;│── benchmark.py   <-- Your benchmarking script       
│&emsp;&emsp;│── utils.py       <-- Utility functions (e.g., load_usernames)     
│&emsp;&emsp;│── base_algorithm.py  <-- Defines an abstract base class for search algorithms      
│&emsp;&emsp;│── linear_search.py  <-- Implementation of Linear search    
│&emsp;&emsp;│── binary_search.py  <-- Implementation of Binary search    
│&emsp;&emsp;│── hashing.py  <-- Implementation of Hashing     
│&emsp;&emsp;│── bloom_filter.py  <-- Implementation of Bloom Filter     
│&emsp;&emsp;│── cuckoo_filter.py  <-- Implementation of Cuckoo Filter     
│&emsp;&emsp;│── cuckoo_bucket.py  <-- Implementation of Cuckoo Bucket       
│       
│── 📂 tests/  <-- Unit tests     
│&emsp;&emsp;│── test_search_algorithms.py  <-- Unit tests for the Linear and Binary search algorithms    
│&emsp;&emsp;│── test_hashing.py  <-- Unit tests for Hashing      
│&emsp;&emsp;│── test_bloom_filter.py  <-- Unit tests for the Bloom Filter      
│&emsp;&emsp;│── test_cuckoo_filter.py  <-- Unit tests for the Cuckoo Filter      
│&emsp;&emsp;│── test_cuckoo_bucket.py  <-- Unit tests for the Cuckoo Bucket      
│      
│── README.md       
│── login_checker.py  <-- File containing main Python script             
│── requirements.txt  <-- Project requirements           

## Setup instructions   

## References
Cuckoo filters were originally described in:       
        Fan, B., Andersen, D. G., Kaminsky, M., & Mitzenmacher, M. D. (2014, December).
        Cuckoo filter: Practically better than bloom.
        In Proceedings of the 10th ACM International on Conference on emerging Networking Experiments and Technologies (pp. 75-88). ACM.

Code in CuckooFilter and CuckooBucket classes was adapted from:      
Michael The1. python-cuckoo. Accessed: 2025-02-05. 2020. url: https://github.com/michael-the1/python-cuckoo/tree/master.

Code in BloomFilter class was adapted from:     
GeeksforGeeks. Bloom Filters - Introduction and Python Implementation.
Accessed: 2025-01-25. 2020. url: https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
