
def make_suffix_array(input):
	suff = [(i, input[i:]) for i in range(len(input))]

	# given pairs (index, string), sort by string
	suff.sort(key=lambda x: x[1])

	# create array of just indexes
	suffix_arr = [i for i, s in suff]

	return suffix_arr

def find_last_char(input, suff_indexes):
    bwt = ""
    l = len(input)

    for i in range(l):
	    j = suff_indexes[i] - 1
	    if j < 0:
		    j = j + l
	    bwt += input[j]

    return bwt

def make_runs(string):
    runs = []
	
    # init
    current_run = string[0]
    run_length = 1
    
    for char in string[1:]:
        if char == current_run:
            run_length += 1
        else:
            runs.append((current_run, run_length))
            current_run = char
            run_length = 1
    
    # add the last run
    runs.append((current_run, run_length))
    
    return runs

def make_bwt(input):

    suff_indexes = make_suffix_array(input)
    bwt = find_last_char(input, suff_indexes)
    runs = make_runs(bwt)

    return bwt, runs


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
        "ABRACADABRA",
        "BANANA",
        "MISSISSIPPI"
    ]

    for s in random_strings:
        bwt, runs = make_bwt(s)
        print(s)
        print("BWT: ", bwt)
        print("number of runs: ", len(runs))
        print('\n')

if __name__ == "__main__":
    main()