import matplotlib.pyplot as plt
import random

from plot_lengths import binary_length, gamma_length, delta_length, fibonacci_length, rice_length

def print_lengths(lengths):
    t = [
        'binary',
        'gamma',
        'delta',
        'fibonacci',
        'rice k=5',
        'rice k=7'
    ]
    for i,l in enumerate(lengths):
        print(f'{t[i]}: {l}')
    print('\n\n')

def plot_histogram(lengths):
    titles = [
        'binary',
        'gamma',
        'delta',
        'fibonacci',
        'rice k=5',
        'rice k=7'
    ]
    plt.bar(titles, lengths, color='blue', edgecolor='black')
    plt.xlabel('Code')
    plt.ylabel('Number of bits')
    # plt.title('')
    plt.show()

# Report the statistics on the following experiments:

def integers100():

    # + Number of bits required to encode 100 integers between 1 and
    # 100,000 (Consider integers 1, 1011, 2021, ...)

    binary_lengths = 0
    gamma_lengths = 0
    delta_lengths = 0
    fibonacci_lengths = 0
    rice5_lengths = 0
    rice7_lengths = 0

    for i in range(1,100):
        n = 1 + (i * 1010)
        binary_lengths += binary_length(n)
        gamma_lengths += gamma_length(n)
        delta_lengths += delta_length(n)
        fibonacci_lengths += fibonacci_length(n)
        rice5_lengths += rice_length(n,5)
        rice7_lengths += rice_length(n,7)

    lengths = [
        binary_lengths, 
        gamma_lengths, 
        delta_lengths,
        fibonacci_lengths,
        rice5_lengths,
        rice7_lengths
    ]

    print_lengths(lengths)

    plot_histogram(lengths)

def random_integers(limit):

    # + Number of bits required to compress 100 random integers between
    # 1 and 1000.

    binary_lengths = 0
    gamma_lengths = 0
    delta_lengths = 0
    fibonacci_lengths = 0
    rice5_lengths = 0
    rice7_lengths = 0

    for _ in range(1,100):
        n = random.randint(1, limit)
        binary_lengths += binary_length(n)
        gamma_lengths += gamma_length(n)
        delta_lengths += delta_length(n)
        fibonacci_lengths += fibonacci_length(n)
        rice5_lengths += rice_length(n,5)
        rice7_lengths += rice_length(n,7)

    lengths = [
        binary_lengths, 
        gamma_lengths, 
        delta_lengths,
        fibonacci_lengths,
        rice5_lengths,
        rice7_lengths
    ]

    print_lengths(lengths)

    plot_histogram(lengths)


def distribution():

    # + Number of bits required to encode a 
    # sequence of 1000 integers with 
    # a distribution chosen in advance

    binary_lengths = 0
    gamma_lengths = 0
    delta_lengths = 0
    fibonacci_lengths = 0
    rice5_lengths = 0
    rice7_lengths = 0

    random_numbers = [int(random.gauss(mu=50000, sigma=10000)) for _ in range(1000)]
    # numbers between 1 and 100000
    random_numbers = [min(max(number, 1), 100000) for number in random_numbers]

    for n in random_numbers:
        binary_lengths += binary_length(n)
        gamma_lengths += gamma_length(n)
        delta_lengths += delta_length(n)
        fibonacci_lengths += fibonacci_length(n)
        rice5_lengths += rice_length(n,5)
        rice7_lengths += rice_length(n,7)

    lengths = [
        binary_lengths, 
        gamma_lengths, 
        delta_lengths,
        fibonacci_lengths,
        rice5_lengths,
        rice7_lengths
    ]

    print_lengths(lengths)

    plot_histogram(lengths)

def main():
    print('INTEGERS 1-100000')
    print('-----------------')
    integers100()
    print('RANDOM INTEGERS 1-1000')
    print('---------------')
    random_integers(1000)
    print('INTEGERS NORMAL DISTRIBUTION')
    print('----------------------------')
    distribution()


if __name__ == "__main__":
    main()


