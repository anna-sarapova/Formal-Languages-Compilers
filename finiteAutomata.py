#read csv
with open('csv_file.csv', 'r') as f:
    lines_list = f.readlines()

    string_split = [ elem.strip().split('->') for elem in lines_list]

grammar = {}
for pair in string_split:
    key = pair[0]
    value = pair[-1]

    is_key_in_grammar = bool(grammar.get(key))

    if is_key_in_grammar:
       # print(f"grammar already contains {key}! Appending..")
        grammar.get(key).append(value)
    else:
       # print(f"grammar does not have {key}! Creating new list..")
        grammar[key] = [value]

print(grammar)

def fetus(current_productions, current_letter):
    """ Searches for elements in current_productions that start with current_letter """
    return [elem for elem in current_productions if elem[0] == current_letter]


def word_check(grammar, word):
    stack = ["S"]
    # current_pointer = 0

    while len(stack):
        popped = stack.pop()
        current_pointer = len(popped) - 1

        print(popped)

        if word == popped:
            return True

        if current_pointer >= len(word):
            continue

        current_letter = word[current_pointer]
        current_non_terminal = popped[-1]
        current_productions = grammar.get(current_non_terminal, [])
        to_push = fetus(current_productions, current_letter)

        popped = popped[:-1]

        to_push = [popped + elem for elem in to_push]
        stack.extend(to_push)

    return False

# grammar = {
#     "S": ["aB", "bB"],
#     "B": ["bD", "cB", "aS"],
#     "D": ["b", "aD"]
# }

assert word_check(grammar, "acbab")
# assert word_check(grammar, "abab")
# assert word_check(grammar, "bcabbb")
#
# assert not word_check(grammar, "aaaaa")
# assert not word_check(grammar, "ac")
# assert not word_check(grammar, "acbaa")
