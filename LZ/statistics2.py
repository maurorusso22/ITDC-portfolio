from math import pow
from BWT import make_bwt
from LZ77 import compress as LZ77

def build_fibonacci_till(index):
	f = [0 for i in range(index)]
	f[0] = 0
	f[1] = 1
	i = 2

	while i < index:
		f[i] = f[i - 1] + f[i - 2]
		i += 1

	return f

def fibonacci_odd(f):
    return list(filter(lambda x: x % 2 != 0, f))

def fibonacci_even(f):
    return list(filter(lambda x: x % 2 == 0, f))

def make_word_Tk(i=3, k=1):
    # k > 0, i >= 1
    a = 'a'
    b = 'b'
    w = ''
    for j in range(1, i + 1):
        w += a + (int(pow(j,k)) * b)
    return w

def words_Tk(limit = 4):
    result = []
    for k in range(1, limit):
        w = make_word_Tk(3, k)
        result.append(w)
    return result

def make_word_Wk(k=6):
    # k > 5
    a = 'a'
    aa = 'aa'
    b = 'b'
    w = ''

    for i in range(2, k):
        si = a + (i*b) + aa
        ei = a + (i*b) + a + b + ((i-2)*a)
        w += si + ei

    qk = a + (k*b) + a
    w += qk

    return w

def words_Wk(limit = 9):
    result = []
    for k in range(6, limit):
        w = make_word_Wk(k)
        result.append(w)
    return result


def calc_r_z(words):
    print('WORDS')
    print(words)
    print()
    for s in words:
        n = len(s)
        bwt, runs = make_bwt(s)
        lz77 = LZ77(s)

        r = len(runs)
        z = len(lz77)

        print("string: ", s)
        print("BWT: ", bwt)
        print("LZ77: ", *lz77, sep=' ')
        print()
        print("number of runs: ", r)
        print("number of triplets: ", z)
        print('--------------------\n')
        
    print('\n\n')

def main():
    # Compute the value of z and r for the following binary words 
    # + the words Tk
    # + the Fibonacci words of odd order 
    # + The Fibonacci words of even order
    # + Given an integer k>5, the set of the word Wk

    f = build_fibonacci_till(30)
    odd = fibonacci_odd(f)
    even = fibonacci_even(f)
    Tk = words_Tk()
    Wk = words_Wk()

    bin_odd = list(map(lambda x: f'{x:b}', odd))
    bin_even = list(map(lambda x: f'{x:b}', even))

    calc_r_z(Tk)
    calc_r_z(bin_odd)
    calc_r_z(bin_even)
    calc_r_z(Wk)

if __name__ == "__main__":
    main()