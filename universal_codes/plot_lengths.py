import matplotlib.pyplot as plt

from math import log
from math import floor
  
log2 = lambda n: log(n, 2) 

from fibonacci import encode as fibonacci
from rice import quotient

# Plot for each n=1,..1000 the lengths of the binary, gamma, delta, Fibonacci codes. 
# Also consider the Rice encoding for k=5 and k=7

def binary_length(n):
    return n.bit_length()

def gamma_length(n):
    # 2|log2 𝑥| + 1
    return 2 * floor(log2(n)) + 1

def delta_length(n):
    # 1 + 2|log2(|log2 x| + 1)|) + |log2 x|
    return 1 + 2*floor(log2(floor(log2(n) + 1))) + floor(log2(n))

def fibonacci_length(n):
    return len(fibonacci(n))

def rice_length(n, k):
    # The bit length of Rk(x) is q + k + 1
    q = quotient(n,k)
    return q + 1 + k

def plot_code_lengths():
    x = list(range(1, 1001))

    binary_lengths = [binary_length(n) for n in x]
    gamma_lengths = [gamma_length(n) for n in x]
    delta_lengths = [delta_length(n) for n in x]
    fibonacci_lengths = [fibonacci_length(n) for n in x]
    rice5_lengths = [rice_length(n,5) for n in x]
    rice7_lengths = [rice_length(n,7) for n in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, binary_lengths, label='Binary')
    plt.plot(x, gamma_lengths, label='Gamma')
    plt.plot(x, delta_lengths, label='Delta')
    plt.plot(x, fibonacci_lengths, label='Fibonacci')
    plt.plot(x, rice5_lengths, label='Rice (k=5)')
    plt.plot(x, rice7_lengths, label='Rice (k=7)')

    plt.xlabel('n')
    plt.ylabel('Length')
    plt.title('Length of Different Codes for n=1 to 1000')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    plot_code_lengths()

if __name__ == "__main__":
    main()