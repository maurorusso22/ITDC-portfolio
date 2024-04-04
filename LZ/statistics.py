import matplotlib.pyplot as plt
import random
import string
from math import log, pow

from BWT import make_bwt
from LZ77 import compress as LZ77

log2 = lambda n: log(n, 2) 

def main():

    # Compare the number of triplets denoted by z produced by LZ77(T) (or by LZss) 
    # and the number of the equal-letter runs denoted by r produced by the BWT(T). 
    # Test experimentally whether the following relations hold:
    # + r = 0(zlog2n)
    # + z = 0(rlogn),
    # where n is the length of the input random_string
    
    triplets_numbers = []
    runs_numbers = []
    f_zlog2n= []
    f_rlogn = []

    min_length=10
    max_length=100
    # create random strings
    for i in range(min_length,max_length):
        random_string = ''.join(random.choices(string.ascii_lowercase, k=i))

        n = len(random_string)
        bwt, runs = make_bwt(random_string)
        lz77 = LZ77(random_string)

        # number of the equal-letter runs denoted by r
        r = len(runs)
        # number of triplets denoted by z
        z = len(lz77)

        
        # save the results in 2 arrays
        triplets_numbers.append(z)
        runs_numbers.append(r)

        # values to plot after
        f_zlog2n.append(z * pow(log2(n), 2)) # (z log2 n)
        f_rlogn.append(r * log2(n)) # (r log n)
        
    # Compare the number of triplets denoted by z produced by LZ77(T) (or by LZss) 
    # and the number of the equal-letter runs denoted by r produced by the BWT(T). 
    plt.plot(range(min_length,max_length), triplets_numbers, label = "triplets LZ77")
    plt.plot(range(min_length,max_length), runs_numbers, label = "runs BWT")
    plt.legend()
    plt.title('Comparison number of triplets - number of runs')
    plt.ylabel('triplets - runs')
    plt.xlabel('String Length')
    plt.show()

    # Test experimentally whether the following relations hold:
    # + r = 0(z log2 n)
    # + z= 0(r log n),
    # where n is the length of the input text

    # z = O(r log n) is verified if r log n is an upper bound for z,
    # so graphically, z must be "under" r log n
    plt.plot(range(min_length,max_length), triplets_numbers, label = "z")
    plt.plot(range(min_length,max_length), f_rlogn, label = "(r log n)")
    plt.title('z = O(r log n)')
    plt.ylabel('triplets - runs')
    plt.xlabel('String Length')
    plt.legend()
    plt.show()

    # r = O(z log^2 n) is verified if z log^2 n is an upper bound for r,
    # so graphically, r must be "under" z log^2 n
    plt.plot(range(min_length,max_length), runs_numbers, label = "r")
    plt.plot(range(min_length,max_length), f_zlog2n, label = "(z log^2 n)")
    plt.title('r = O(z log^2 n)')
    plt.ylabel('triplets - runs')
    plt.xlabel('String Length')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()