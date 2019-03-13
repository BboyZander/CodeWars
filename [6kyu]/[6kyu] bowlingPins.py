def bowlingPins(arr):
    result = ""
    line = [[],[],[],[]]
    for x in range(7,11):
        line[0].append(" ") if x in arr else line[0].append("I")
    result = " ".join(line[0]) + "\n"

    for x in range(4,7):
        line[1].append(" ") if x in arr else line[1].append("I")
    result += " " + " ".join(line[1]) + " \n"

    for x in range(2,4):
        line[2].append(" ") if x in arr else line[2].append("I")
    result += "  " + " ".join(line[2]) + "  \n"

    line[3].append(" ") if 1 in arr else line[3].append("I")
    result += "   " + " ".join(line[3]) + "   "
    return result


pins = "{7} {8} {9} {10}\n" + \
        " {4} {5} {6} \n" + \
         "  {2} {3}  \n" + \
          "   {1}   "

def bowling_pins(arr):
    return pins.format(*(" " if i in arr else "I" for i in range(11)))

print(bowlingPins([1, 2, 3]))
print(bowling_pins([1, 2, 3]))