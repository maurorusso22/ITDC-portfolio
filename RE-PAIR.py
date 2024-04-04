
# uppercase alphabet as symbols
SYMBOLS = [chr(i) for i in range(65, 91)]

def make_pairs(string):
    pairs = {}
    last_pair = ''

    # find and count the frequencies
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        if pair != last_pair: # to avoid overlap
            try:
                if pairs[pair]:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1
            except:
                pairs[pair] = 1
        last_pair = pair
    
    pairs = list(pairs.items())

    # keep only the pairs that appear more than once
    pairs = list(filter(lambda p: p[1] > 1, pairs))

    # sort by frequencies
    pairs.sort(key=lambda p: p[1], reverse=True)

    return pairs

def make_grammar(input):
    string = input
    symbols = SYMBOLS.copy()
    grammar = []

    while True:
        pairs = make_pairs(string)
        if (pairs):
            # Identify symbols X and Y such that XY is the most frequent
            # pair.
            last_pair = pairs[0][0]

            # Introduce a new symbol A and 
            symbol = symbols.pop(0)
            rule = (symbol, last_pair)
            grammar.append(rule)

            # replace all occurrences of XY with A
            string = string.replace(last_pair, symbol)

        else:
            # If no pair appears
            # more than once, stop

            # define the start symbol
            last_rule = ('STRING', string)
            grammar.append(last_rule)

            return grammar
        
def make_cnf_grammar(string):

    # Una grammatica in Forma Normale di Chomsky (CNF) è una grammatica formale 
    # in cui ogni regola di produzione ha uno dei due seguenti formati:

        # 1) Un non-terminale che si traduce direttamente in un terminale: A → a, 
        # dove A è un non-terminale e a è un terminale.
        
        # 2) Un non-terminale che si traduce in due non-terminali: A → BC, 
        # dove A, B e C sono non-terminali.

    # In una grammatica CNF, l'unica eccezione a queste regole è 
    # la produzione di partenza (start symbol), 
    # che può tradursi anche in ε (il simbolo vuoto), 
    # ma questa è l'unica occorrenza di ε permessa in una grammatica CNF.

    # esempio grammatica CNF:
    # S → AB | BC
    # A → a
    # B → b
    # C → c


    # All terminal symbols in the input string are replaced with non-
    # terminal symbols. This creates unary productions
    symbols = SYMBOLS.copy()
    grammar = []
    chars = sorted(list(set(string)))

    for c in chars:
        symbol = symbols.pop(0)
        rule = (symbol, c)
        grammar.append(rule)

        string = string.replace(c, symbol)


    # Replacement step: The algorithm picks an arbitrary bigram which has the most
    # nonoverlapping occurrences in the string, and then replaces all possible
    # occurrences of the bigram with a new non-terminal symbol
        
    while True:
        pairs = make_pairs(string)
        if (pairs):
            # Identify symbols X and Y such that XY is the most frequent
            # pair.
            last_pair = pairs[0][0]

            # Introduce a new symbol A and 
            symbol = symbols.pop(0)
            rule = (symbol, last_pair)
            grammar.append(rule)

            # replace all occurrences of XY with A
            string = string.replace(last_pair, symbol)

        else:
            # The algorithm repeats the same process recursively for the string 
            # obtained after the replacement of the bigrams, 
            # until no bigrams have two or more non-overlapping occurrences in the string.
            # It is clear that the productions created in the replacement stage are all binary

            # define the start symbol
            last_rule = ('STRING', string)
            grammar.append(last_rule)
            return grammar

def calc_grammar_size(grammar):
    # The size of a grammar is defined as the total number of symbols on
    # the right-hand side of all rules

    sum = 0
    for rule in grammar:
        right_side = rule[1]
        sum += len(right_side)
    return sum

def print_grammar(rules):
    for rule in rules:
        print(f"{rule[0]} -> {rule[1]}")

def main():
    input = 'a_rose_is_a_rose' # _ = whitespace
    # input = 'aaabcaabaaabcabdabd'
    grammar = make_grammar(input)
    cnf_grammar = make_cnf_grammar(input)

    print('string: ', input)
    print()
    print_grammar(grammar)
    print('grammar size: ', calc_grammar_size(grammar))
    print()
    print_grammar(cnf_grammar)
    print('CNF grammar size: ', calc_grammar_size(cnf_grammar))
    print()

if __name__ == "__main__":
    main()
