from math import log
from math import floor
  
log2 = lambda n: log(n, 2) 
  
def zeros(n): 
    return (floor(log2(n)))*'0'
  
def binary(n):
    return f'{n:b}'
      
def gamma(n): 
    if (n == 0):  
        return '0' 
  
    return zeros(n) + binary(n)

def delta(n):
    if (n == 0):  
        return '0' 
    
    e = floor(log2(n))
    return gamma(e+1) + binary(n)[1:]

def make_encoding(limit, method):
    d = dict()
    for n in range(limit):
        d[n] = method(n)
    return d

def encode(n, encoding):
    return encoding[n]

def decode_gamma(encoded):
    # get prefix length
    prefix_length = 0
    while encoded[prefix_length] != '1':
        prefix_length += 1

    # get suffix
    suffix = '1' + encoded[prefix_length + 1 : prefix_length * 2 + 1] 
    # and convert to decimal 
    decoded = int(suffix, 2)
    return decoded


def decode_delta(encoded): 
    encoded = list(encoded) 

    prefix_length = 0
    while encoded[prefix_length] != '1':
        prefix_length += 1
      
    encoded = encoded[2 * prefix_length + 1 :]  
    # prepend 1
    encoded.insert(0,'1')  

    # convert to decimal
    decoded = int(''.join([x for x in encoded]), 2)
      
    return decoded

def main_gamma():
    encoding = make_encoding(30, gamma)
    print(*encoding.items(), sep='\n')
    for x in range(1,30):
        encoded = encode(x, encoding)
        decoded = decode_gamma(encoded)
        print(x == decoded)

def main_delta():
    encoding = make_encoding(30, delta)
    print(*encoding.items(), sep='\n')
    for x in range(2,30):
        encoded = encode(x, encoding)
        decoded = decode_delta(encoded)
        print(x == decoded)

def main():
    print('GAMMA CODE')
    main_gamma()
    print('\nDELTA CODE')
    main_delta()

if __name__ == "__main__":
    main()