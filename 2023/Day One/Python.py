import re
line_txt_array = open("file.txt").read().split("\n")
part = True # True -> part one, False -> part two
numberdict = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
sommaTotal = 0

stringToInt = lambda string: str(numberdict.index(string)+1) if string in numberdict else string
    
for line_txt in line_txt_array:
    value_str = re.findall("(\d|"+"|".join(numberdict)+")" if part else "(\d)", line_txt)
    stringline = stringToInt(value_str[0])+stringToInt(value_str[-1])
    sommaTotal += int(stringline)
    print(stringline)
print(sommaTotal)