SIZE = 100

def build_fibonacci_till(index):
	f = [0 for i in range(index)]
	f[0] = 1 # fib[0] stores 2nd fibonacci number
	f[1] = 2 # fib[1] stores 3rd fibonacci number
	i = 2

	while i < index:
		f[i] = f[i - 1] + f[i - 2]
		i += 1

	return f

fib = build_fibonacci_till(SIZE)

def largest_fibonacci_number(n):
	i = 2
	while fib[i - 1] <= n:
		i += 1

	# return index of the largest fibonacci number
	# smaller than or equal to n
	return (i - 2)

def encode(n):
	if n == 0:
		return '0'
	
	# Find the largest Fibonacci number equal to or less than N; 
	# subtract this number from N, keeping track of the remainder.
	index = largest_fibonacci_number(n)

	# allocate memory for codeword
	codeword = ['x' for x in range(index + 2)]

	i = index

	while (n):
		
		# If the number subtracted was the ith Fibonacci number F(i), put a 1
		# in place i in the codeword (counting the left most digit as place
		# 0).
		codeword[i] = '1'

		# Repeat the previous steps, substituting the remainder for N, until
		# a remainder of 0 is reached
		n = n - fib[i]

		# Move to Fibonacci just smaller than new n
		i = i - 1

		# Mark all Fibonacci > n as not used (0 bit),
		# progress backwards
		while (i >= 0 and fib[i] > n):
			codeword[i] = '0'
			i = i - 1

	# Place an additional 1 after the rightmost digit in the codeword.
	codeword[index + 1] = '1'

	return "".join(codeword)

def decode(encoded):
	# remove the final "1"
	encoded = encoded[:-1]

	# assign the remaining the values 1,2,3,5,8,13... (the Fibonacci
	# numbers) to the bits in the code word, and sum the values of
	# the "1" bits.
	sum = 0
	for i,c in enumerate(encoded):
		if (c == '1'):
			sum += fib[i]
	return sum

def main():
	for i in range(1, SIZE):
		e = encode(i)
		d = decode(e)
		print(i, e, d, i == d)

if __name__ == "__main__":
    main()