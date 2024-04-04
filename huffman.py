from collections import Counter

def make_encoding(node, bin=''):
    # IDEA: starting from the root, 
    # get the children until they are just strings.
    # When the child is a string, return its encoding
    if type(node) is str:
        return {node: bin}
    (l, r) = node
    d = dict()
    d.update(make_encoding(l, bin + '0')) # 0 to the left
    d.update(make_encoding(r, bin + '1')) # 1 to the right
    return d


def make_tree(nodes):
    while len(nodes) > 1:
        # dequeue last 2 nodes
        (k1, p1) = nodes[-1]
        (k2, p2) = nodes[-2]
        nodes = nodes[:-2]

        # join last 2 nodes
        node = (k1, k2)

        # append and sort the updated list
        nodes.append((node, p1 + p2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    # return the root, which is a "recursive" tuple with all symbols
    return nodes[0][0]

def encode(string, encoding):
    return ''.join([encoding[x] for x in string])

def decode(encoded, tree):
    decoded_text = ''
    current_node = tree
    for bit in encoded:
        if bit == '0':
            current_node = current_node[0] # left child
        else:
            current_node = current_node[1] # right child
        
        if type(current_node) is str:
            decoded_text += current_node
            current_node = tree  # Reset to root for next character
    return decoded_text


def huffman(string):
    # scan the entire input counting frequencies
    freq = dict(Counter(string))

    # calculate probabilities as occurrences / string-length
    freq = [(k, (v / len(string) )) for k,v in freq.items()]

    # and sort them by probability in descending order
    freq = sorted(freq, key=lambda x: x[1], reverse=True)
    
    tree = make_tree(freq)

    encoding = make_encoding(tree)

    for i in encoding:
        print(f'{i}: {encoding[i]}')

    encoded = encode(string, encoding)
    decoded = decode(encoded, tree)

    print()
    print(string)
    print(encoded)
    print(decoded)
    print(f'Success: {string == decoded}\n')

def main():
    random_strings = [
        "ABCADAADBAACB",
        "ACCDADADCB",
        "BBABABBBAC",
        "DCDABDBBAC",
        "ABCDACBBDC",
        "DDBACABDBA",
        "BCBCADACCD",
        "ADADBBACDA",
        "BCDCCABADA",
        "ADBBBCDCBD",
        "CDAABBCBDA",
        "CADABBADBB",
        "BCCABDACDB",
        "DACBACABCD",
        "CDBDADADBC",
        "BCDDAABABB",
        "BACDDDCBBC",
        "DCBABBDBAC",
        "CBBACBBBDA",
        "DDCABDBDAD",
        "AACCDDBBDA"
    ]

    for s in random_strings:
        huffman(s)

main()