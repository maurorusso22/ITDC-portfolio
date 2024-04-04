CODE_TEST = set(['a', 'c', 'ad', 'abb', 'bad', 'deb', 'bbcde']) # F

CODE_0 = set(['012', '0123', '4', '310','1024', '2402', '2401', '4013']) # T
CODE_1 = set(['10', '010', '1', '1110']) # F
CODE_2 = set(['0', '001', '101', '11']) # T
CODE_3 = set(['0', '2', '03', '011', '104', '341', '11234']) # T
CODE_4 = set(['01', '10', '001', '100', '000', '111']) # F

CODES = [CODE_TEST, CODE_0, CODE_1, CODE_2, CODE_3, CODE_4]

def create_suffixes_set(c, n):
    if n == 0:
        # s_of_0 is always c
        return set(c)
    
    else:
        s_of_n = set() # init
        s_of_n_minus_1 = create_suffixes_set(c, n - 1)

        for cw in c:
            for cw1 in s_of_n_minus_1:
                if (len(cw) > len(cw1)) and cw.find(cw1) == 0:
                    # if cw starts with cw1
                    # then add the suffix to s_of_n
                    suffix = cw[ len(cw1) : ]
                    s_of_n.add(suffix)

        # same thing but reversed
        for cw1 in s_of_n_minus_1:
            for cw in c:
                if len(cw1) > len(cw) and cw1.find(cw) == 0:
                    suffix = cw1[ len(cw) : ]
                    s_of_n.add(suffix)

        return s_of_n
    
def check_c1(c, s_of_n):
    # condition 1: if the intersection between s_of_0 and s_of_i is not empty, then C is NOT UD
    return len(c.intersection(s_of_n)) != 0

def check_c2(s_of_n):
    # condition 2: if exists an empty suffix set, then C is UD
    return len(s_of_n) == 0

def check_c3(suffixes):
    # condition 3: if exists a couple i,j such that s_of_i = s_of_j, then C is UD
    for i,x in enumerate(suffixes[1:]): # remove s_of_0
        for j,y in enumerate(suffixes[1:]):
            if i != j != 0 and len(x) != 0 and x == y:
                return True
    
def check_sf(c):
    last_size = 99 # flag to stop the while loop
    suffixes = []
    i = 0
    flagResult = True

    while (last_size > 0 and flagResult):
        s_of_i = create_suffixes_set(c, i)
        suffixes.append(s_of_i)

        # all the conditions hold if i > 0
        if (i > 0 and check_c1(c, s_of_i)):
            print(f'{c} is NOT UD for condition 1')
            flagResult = False
        if (i > 0 and check_c2(s_of_i)):
            print(f'{c} is UD for condition 2')
            flagResult = False
        if (i > 0 and check_c3(suffixes)):
            print(f'{c} is UD for condition 3')
            flagResult = False

        last_size = len(s_of_i)
        i = i + 1

    return

    
def main():
    for C in CODES:
        check_sf(C)

main()