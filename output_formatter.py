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

puzzle = """["Aretha Franklin" = [["areath"], ["rninkalf"]], "Jimi Hendrix" = [["jimi"], ["xdrnhie"]], "Whitney Houston" = [["inewhyt"], ["uohston"]], "Jay-Z" = [["-zjya"]], "Paul Simon & Art Garfunkel" = [["pula"], ["smino"], ["&"], ["tar", "rat"], ["elkrungaf"]], "Drake" = [["raked"]], "Carter Family" = [["tracer", "crater"], ["imafyl"]], "Ella Fitzgerald" = [["leal"], ["liarfzgtde"]], "George Jones" = [["oeggre"], ["ensoj"]], "Willie Nelson" = [["wleiil"], ["lsnnoe"]], "Billie Holiday" = [["iibell"], ["alhoydi"]], "Dolly Parton" = [["yodll"], ["tarpon", "patron"]], "Eddy Arnold" = [["dyed"], ["ladron", "ronald"]], "Big Joe Turner" = [["bgi"], ["eoj"], ["return"]], "Prince" = [["pincer"]], "Pink Floyd" = [["kpin"], ["dofly"]], "Hank Williams" = [["ankh", "khan"], ["ilmlwsai"]], "Louis Jordan" = [["uosli"], ["jonrda"]], "Creedence Clearwater Revival" = [["rcnceedee"], ["ralerawcte"], ["ealvvri"]], "Johnny Cash" = [["hnyjno"], ["csah"]], "Mariah Carey" = [["rmiaha"], ["yacre"]], "Muddy Waters" = [["dydmu"], ["waster", "rawest", "tawers"]], "Otis Redding" = [["otis"], ["grinded"]], "The Miracles" = [["het"], ["reclaims", "claimers"]], "Dizzy Gillespie" = [["zzyid"], ["llesgepii"]], "Bing Crosby" = [["igbn"], ["bocysr"]], "Garth Brooks" = [["agtrh"], ["korobs"]], "Madonna" = [["nandmoa"]], "Beach Boys" = [["cehab"], ["bosy"]], "Howlin' Wolf" = [["wihnl'o"], ["fowl", "flow"]], "Sam Cooke" = [["mas"], ["kcoeo"]], "Bessie Smith" = [["iesbes"], ["smith"]], "Mills Brothers" = [["lmsil"], ["rtbesohr"]], "Temptations" = [["tempotsnati"]], "Beatles" = [["esaeblt"]], "Marvin Gaye" = [["mvianr"], ["gaye"]], "Charlie Parker" = [["aihrecl"], ["reakpr"]], "James Brown" = [["amsej"], ["nwobr"]], "David Bowie" = [["divad"], ["beiow"]], "Drifters" = [["firtders"]], "Johnny Mathis" = [["ojnhny"], ["hsmtai"]], "Thelonious Monk" = [["oitnolhseu"], ["kmon"]], "Bruce Springsteen" = [["cuber"], ["nregeissptn"]], "Michael Jackson / Jackson 5" = [["hmaiecl"], ["jkocsna"], ["/"], ["akocsjn"], ["5"]], "John Coltrane" = [["nojh"], ["onractle"]], "Chuck Berry" = [["cckhu"], ["erbyr"]], "Benny Goodman" = [["benyn"], ["oogdanm"]], "Frank Sinatra" = [["fankr"], ["artisan", "tsarina"]], "2 Pac" = [["2"], ["cap"]], "Ink Spots" = [["kin"], ["stops", "posts"]], "Scott Joplin" = [["tstco"], ["njpiol"]], "Jelly Roll Morton" = [["lejyl"], ["rlol"], ["otnmor"]], "B.B. King" = [["b.b."], ["gikn"]], "Bob Marley and the Wailers" = [["obb"], ["lmarye"], ["dan"], ["het"], ["rwseail"]], "Public Enemy" = [["upiclb"], ["yemen"]], "Bo Diddley" = [["ob"], ["ddyield"]], "Kanye West" = [["kenya"], ["stew", "wets"]], "Bob Dylan" = [["bbo"], ["dlany"]], "Patsy Cline" = [["pasty"], ["elcni"]], "Glenn Miller" = [["lngne"], ["ilrmle"]], "U2" = [["u2"]], "Paul Whiteman" = [["palu"], ["htaiewmn"]], "Eric Clapton" = [["rice"], ["naltcop"]], "Eagles" = [["slgeea"]], "Rod Stewart" = [["rdo"], ["swatter"]], "Tommy Dorsey" = [["tymmo"], ["dsreyo"]], "Ray Charles" = [["rya"], ["larches", "clasher"]], "Nat King Cole" = [["ant", "tan"], ["gnki"], ["ecol"]], "Tony Bennett" = [["ntoy"], ["btentne"]], "Woody Guthrie" = [["dowoy"], ["grtuhei"]], "Abba" = [["baba"]], "Elvis Presley" = [["evils", "veils", "levis", "lives"], ["yelpers"]], "Barbra Streisand" = [["barrab"], ["tardiness"]], "Robert Johnson" = [["eortrb"], ["ooshnjn"]], "Jerry Lee Lewis" = [["yerjr"], ["eel"], ["wiles"]], "Jimmie Rodgers" = [["eijmim"], ["rrdoseg"]], "Nirvana" = [["vnarian"]], "Al Jolson" = [["la"], ["noojls"]], "Perry Como" = [["pryer"], ["oomc"]], "Led Zeppelin" = [["eld", "del"], ["nzeilepp"]], "The Who" = [["eht"], ["how"]], "The Supremes" = [["eth"], ["presumes"]], "Rolling Stones" = [["nillorg"], ["setons", "onsets", "stenos"]], "Enrico Caruso" = [["coiner", "recoin"], ["crauso"]], "Little Richard" = [["lieltt"], ["rrcdahi"]], "Count Basie" = [["tnocu"], ["isabe"]], "Buddy Holly and the Crickets" = [["dydub"], ["lyolh"], ["dan"], ["teh"], ["rskiccte"]], "Elton John" = [["lento"], ["nhoj"]], "Miles Davis" = [["smile", "slime", "limes"], ["divas", "vadis"]], "Stevie Wonder" = [["teevsi"], ["downer"]], "Louis Armstrong" = [["usilo"], ["sgrnomtar"]], "Fats Domino" = [["fast"], ["oinomd"]], "Everly Brothers" = [["rlyvee"], ["htsrreob"]], "Bee Gees" = [["bee"], ["eseg"]], "Eminem" = [["eenmim"]], "Duke Ellington" = [["dkue"], ["nlligotne"]], "Queen" = [["nueqe"]], "Run-D.M.C." = [["..drmn.-uc"]], "Mahalia Jackson" = [["ahaliam"], ["caojksn"]], "Fats Waller" = [["fast"], ["lwrale"]]]"""

output = table_to_puzzle(puzzle)
print(output)