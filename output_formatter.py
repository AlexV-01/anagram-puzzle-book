"""
Input: ["key1" = [["value11", "value12", ...], ["value21", "value22", ...], ...], ...]
Output: value11/value12/... value21/value22/... ...
"""
def table_to_puzzle(table):
    table = table[1:-1] # strip useless brackets
    puzzle = ""

    stack = []
    line = ""
    anagrams = ""
    word = ""
    lines_cleared = 0
    equals_count = 0

    line_over = False
    anagrams_over = False
    word_over = False

    for i in range(len(table)):
        match table[i]:
            case '[':
                stack.append('[')
                line_over = False
            case ']':
                stack.pop()
                line_over = len(stack) == 0
                lines_cleared += 1 if len(stack) == 0 else 0
                anagrams_over = len(stack) == 1
            case '=':
                equals_count += 1
            case '"':
                word_over = table[i+1] == ',' or table[i+1] == ']'
            case " ":
                pass
            case ',':
                pass
            case _:
                if equals_count > lines_cleared:
                    word += table[i]
        if line_over:
            puzzle += line[:-1] + "\n"
            line = ""
            line_over = False
        elif anagrams_over:
            line += anagrams[:-1] + " "
            anagrams = ""
            anagrams_over = False
        elif word_over:
            anagrams += word + "/"
            word = ""
            word_over = False
    return puzzle

puzzle = """["Denver" = [["nerved", "vender"]], "Helena" = [["eleanh"]], "Oklahoma City" = [["kalmooah"], ["iytc"]], "Olympia" = [["oiyampl"]], "Annapolis" = [["snpioalan"]], "Tallahassee" = [["ateesalsalh"]], "Richmond" = [["nrdhcoim"]], "Baton Rouge" = [["tabon"], ["rogue"]], "Jackson" = [["ckjsoan"]], "Harrisburg" = [["ibhusrragr"]], "Dover" = [["roved", "drove"]], "Madison" = [["daimons", "domains"]], "Little Rock" = [["titlle"], ["cork"]], "Juneau" = [["uneaju"]], "Cheyenne" = [["yceeennh"]], "Lansing" = [["lnnasig"]], "Providence" = [["nieeprcovd"]], "Frankfort" = [["kfrtonarf"]], "Boston" = [["ostnbo"]], "Phoenix" = [["ixnpeho"]], "Charleston" = [["sthocleran"]], "Sacramento" = [["rctmoaeasn"]], "Indianapolis" = [["ipilandaions"]], "Raleigh" = [["lrgihea"]], "Montgomery" = [["tnomroymge"]], "Nashville" = [["lsvhnliae"]], "Santa Fe" = [["satan"], ["fe"]], "Topeka" = [["toeakp"]], "Carson City" = [["narcos", "acorns"], ["city"]], "Albany" = [["lnyaab"]], "Salem" = [["males", "lames", "meals"]], "Columbia" = [["oubialcm"]], "Des Moines" = [["eds"], ["monies"]], "Jefferson City" = [["fjneefrso"], ["ctyi"]], "Bismarck" = [["raibckms"]], "Trenton" = [["ntenrto"]], "Augusta" = [["suaguta"]], "Pierre" = [["ierrpe"]], "Atlanta" = [["naltata"]], "Hartford" = [["ratfdorh"]], "Concord" = [["nodoccr"]], "Honolulu" = [["nolhluou"]], "Montpelier" = [["lniorepmet"]], "Saint Paul" = [["antis", "stain", "satin"], ["ualp"]], "Columbus" = [["bosmlcuu"]], "Austin" = [["tsnaiu"]], "Salt Lake City" = [["last", "slat"], ["kale", "leak"], ["icty"]], "Lincoln" = [["nnlcoil"]], "Springfield" = [["glpidefinrs"]], "Boise" = [["oebis"]]]"""

output = table_to_puzzle(puzzle)
print(output)