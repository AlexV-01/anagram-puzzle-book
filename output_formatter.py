"""
Input: ["key1" = [["value11", "value12", ...], ["value21", "value22", ...], ...], ...]
Output: value11/value12/... value21/value22/... ...
"""
def table_to_puzzle(table):
    table = table[1:-1] # strip useless brackets
    puzzle = ""

    stack = []
    line = ""
    anagram = ""
    word = ""

    line_over = False
    anagrams_over = False
    word_over = False

    for c in table:
        match c:
            case '[':
                stack.append('[')
            case ']':
                stack.pop()
            case '=':
                pass
            case '"':
                pass
            case " ":
                pass
            case ',':
                line_over = stack == []
                anagrams_over = stack == ['[']
                word_over = stack == ['[[']
            case _:
                word += c
        if line_over:
            puzzle += line + "\n"
        elif anagrams_over:
            line += anagram[:-1] + " "
        elif word_over:
            anagram += word + "/"
    return puzzle


output = table_to_puzzle("[something]")
print(output)