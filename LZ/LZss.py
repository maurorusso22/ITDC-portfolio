
def compress(input, window_length=4):
    output = []
    seen_input = '' 
    window_begin_index = 0

    while input:
        pair = find_longest_match(input, window_length, seen_input, window_begin_index)
        if (pair):
            output.append(pair)
        
        offset, element = pair

        # if element is int, then it's a lenght
        # otherwise (it's a char) so length = 1
        length = element if type(element) == type(1) else 1

        # update what you have seen so far
        seen_input += input[:(length)]

        # discard chars already seen
        input = input[length:]

        # update the index of the input which will be the 
        # begin index of the window for the next iteration
        window_begin_index += length
    
    return output


def find_longest_match(input, window_length, seen_input, window_begin_index):
    if input is None or input == "":
        return (0, 0)
    
    # init window
    window = input[0:window_length]

    # init
    length = 0
    offset = 0
    window_current_index = 0
    buffer = window[window_current_index]

    while (True):

        # check if there is a match
        if buffer in seen_input:
            # increment window index
            window_current_index += 1

            # find the index of the last match
            index = seen_input.rindex(buffer)

            # find the offset between the begin of the window 
            # and the first char of the match
            offset = window_begin_index - index

            if (window_current_index < len(window)):
                # increment the length of the match
                length += 1

                # if the window has more chars, consider
                # one more char to try to find a longer match
                buffer += window[window_current_index]
            else:
                length = len(buffer)
                # if the window has no more chars, 
                # return the last match info

                return (offset, length)

        else:
            # if there is no match anymore, return
            return (offset, length or buffer[-1])


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
        "AACCDDBBDA",
        "XYXZXXYXZZXXYZZXZ",
        "XYXZXXYXZZXXYZZXXYZX",
        "AACAACABCABAAAC",
        "ABAABABAABB",
        "AABBABAB",
        "La compressione dati viene utilizzata sia per ridurre le dimensioni di un file, e quindi lo spazio necessario per la sua memorizzazione, sia per ridurre l'occupazione di banda necessaria in una generica trasmissione dati digitale come ad esempio una trasmissione televisiva digitale"
    ]

    for s in random_strings:
        output = compress(s)
        print(s)
        print(*output, sep='\n')
        print()

if __name__ == "__main__":
    main()
