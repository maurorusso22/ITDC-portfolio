from math import floor
from math import log
  
log2 = lambda n: log(n, 2) 

k = 7
# 1. Fix the parameter M to an integer value.
M = pow(2, k)

def binary(n, M):
    # Remainder code (in truncated binary encoding)
    # Let b = ⌊log2(M)⌋
    b = floor(log2(M))

    limit = pow(2, b + 1) - M
    if (n < limit):
        # If r<2^{b+1}-M: code r in binary representation using b bits.
        return f'{n:0{b}b}'
    else:
        # If r>=2^{b+1}-M} code the number r+2^{b+1}-M in binary representation using b + 1 bits.
        return f'{(n + limit):0{b+1}b}'

def unary(n):
    # Quotient code (in unary coding)
    # 1. Write a q-length string of 1 bits (alternatively, of 0 bits)
    # 2. Write a 0 bit (respectively, a 1 bit)
    return (n)*'0' + '1'

def quotient(n, k):
    # we will use it for statistics
    M = pow(2, k)
    q = floor( n / M )
    return q

def rice(n, k=7):

    # 1. Set the parameter M
    M = pow(2, k)

    # For N, the number to be encoded, find
    # 1. quotient = q = floor(N/M)
    q = floor( n / M )

    # 2. remainder = r = N modulo M
    r = n % M

    # Generate the code format : <Quotient code><Remainder code>
    encoded = unary(q) + binary(r, M)

    return encoded

def decode(encoded, k=7):

    # 1. Set the parameter M
    M = pow(2, k)

    # Decode the unary representation of q (count the number of 1 in the beginning of the code)
    number_of_0s = 0
    while encoded[number_of_0s] == '0':
        number_of_0s += 1

    q = number_of_0s
    # Skip the 1 delimiter
    encoded = encoded[number_of_0s + 1:]

    # Let b = ⌊log2(M)⌋
    b = floor(log2(M))

    # Interpret next b bits as a binary number r'
    r = int(encoded, 2)

    # if r' < 2^(b+1) - M holds, then the reminder r = r'
    limit = pow(2, b + 1) - M

    if (r < limit):
        pass
    else:
        # Otherwise the reminder is given by r = r'-2^(b+1) + M
        r = r - limit

    # Compute N = q * M + r
    n = q * M + r

    return n


def main():
    for i in range(1, 100):
        k = 7
        e = rice(i, k)
        d = decode(e, k)
        print(i, e, d, i == d)

if __name__ == "__main__":
    main()