nc = int(input())           # Read in number of cases
cases = []                  # Queue that stores cases

for i in range(nc):
    case = input()
    cases.append(case)

ROMAN_NUMERAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}


def converttoint(numeral):
    """ (string) --> int
        Takes a string representation of numeral and converts to int.
    """
    total = 0
    i = 0
    while(i < len(numeral)):
        if not (i == len(numeral) - 1):
            if (numeral[i] == 'I') and (numeral[i+1] == 'V'):
                total += 4
                i += 1
            elif (numeral[i] == 'I') and (numeral[i+1] == 'X'):
                total += 9
                i += 1
            elif (numeral[i] == 'X') and (numeral[i+1] == 'L'):
                total += 40
                i += 1
            elif (numeral[i] == 'X') and (numeral[i+1] == 'C'):
                total += 90
                i += 1
            elif (numeral[i] == 'C') and (numeral[i+1] == 'D'):
                total += 400
                i += 1
            elif (numeral[i] == 'C') and (numeral[i+1] == 'M'):
                total += 900
                i += 1
            else:
                total += ROMAN_NUMERAL[numeral[i]]
        else:
            total += ROMAN_NUMERAL[numeral[i]]

        i += 1
    return total


def converttonumeral(i):
    

for case in cases:
    fnum, snum = case.split('+')
    snum = snum[:-1]

    total = 0
    total += converttoint(fnum)
    total += converttoint(snum)

    print(total)
