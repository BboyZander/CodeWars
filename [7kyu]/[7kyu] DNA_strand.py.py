import string

def DNA_strand(dna):
    strand = dna.upper()
    newstrand = ''
    for i in range(len(dna)):
        if strand[i] == "T":
            newstrand += "A"

        if strand[i] == "A":
            newstrand += "T"

        if strand[i] == "G":
            newstrand += "C"

        if strand[i] == "C":
            newstrand += "G"

    return newstrand


print(DNA_strand('aaattt'))