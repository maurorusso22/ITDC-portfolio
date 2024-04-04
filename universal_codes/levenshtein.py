def binary(n):
    return f'{n:b}'

def levenshtein(n):
    if n == 0:
        return '0'
    
    cw = '' # codeword
    c = 0 # counter
    m = n
    while (m > 0):
        # 1. Initialize the step count variable C to 1.
        c = c + 1
        # 2. Write the binary representation of the number 
        # without the leading "1" to the beginning of the code.
        bin = binary(m)
        bin = bin[1:]
        cw = bin + cw
        # 3. Let M be the number of bits written in step 2.
        m = len(bin)
        # 4. If M is not 0, increment C, 
        # repeat from step 2 with M as the new
        # number.
    
     # 5. Write C "1" bits and a "0" to the beginning of the code.
    string_to_add = c * '1' + '0'
    cw = string_to_add + cw
    return cw

def make_encoding(limit, method):
    d = dict()
    for n in range(limit):
        d[n] = method(n)
    return d

def encode(n, encoding):
    return encoding[n]

def decode(encoded):
    # To decode a Levenstein-coded integer:
    # 1. Count the number of "1" bits until a "0" is encountered.
    number_of_1s = 0
    while encoded[number_of_1s] == '1':
        number_of_1s += 1
    
    # 2. If the count is zero, the value is zero, otherwise
    if (number_of_1s == 0):
        return 0
    
    # discard 1s and the first 0
    encoded = encoded[number_of_1s + 1:]

    # 3. Start with a variable N, set it to a value of 1 and repeat
    # count-1 times:

    N = 1
    for i in range(number_of_1s - 1):
        # 4. Read N bits, prepend "1", assign the resulting value to N
        reading = encoded[:N]
        encoded = encoded[N:]
        reading = '1' + reading
        N = int(reading, 2) # convert to decimal

    return N


def main():
    SIZE = 50
    encoding = make_encoding(SIZE, levenshtein)
    print(*encoding.items(), sep='\n')
    for x in range(1, SIZE):
        encoded = encode(x, encoding)
        decoded = decode(encoded)
        print(x, encoded, decoded, x == decoded)
        print()

if __name__ == "__main__":
    main()