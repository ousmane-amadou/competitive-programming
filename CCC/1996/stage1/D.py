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
    """ (int) -> String
        Takes an integer and converts it into a roman numeral.
    """
    numeral = ""
    if i > 1000:
        numeral = "CONCORDIA CUM VERITATE"
    else:
        digits = list(str(i))
        digits = ['-1']*(4-len(digits)) + digits

        for j in range(4):
            if not digits[j] == '-1':
                if j == 0:
                    numeral = "M"
                elif j == 1:
                    if digits[j] == "1":
                        numeral += 'C'
                    elif digits[j] == "2":
                        numeral += 'CC'
                    elif digits[j] == "3":
                        numeral += 'CCC'
                    elif digits[j] == "4":
                        numeral += 'CD'
                    elif digits[j] == "5":
                        numeral += 'D'
                    elif digits[j] == "6":
                        numeral += 'DC'
                    elif digits[j] == "7":
                        numeral += 'DCC'
                    elif digits[j] == "8":
                        numeral += 'DCCC'
                    elif digits[j] == "9":
                        numeral += 'CM'
                elif j == 2:
                    if digits[j] == "1":
                        numeral += 'X'
                    elif digits[j] == "2":
                        numeral += 'XX'
                    elif digits[j] == "3":
                        numeral += 'XXX'
                    elif digits[j] == "4":
                        numeral += 'XL'
                    elif digits[j] == "5":
                        numeral += 'L'
                    elif digits[j] == "6":
                        numeral += 'LX'
                    elif digits[j] == "7":
                        numeral += 'LXX'
                    elif digits[j] == "8":
                        numeral += 'LXXX'
                    elif digits[j] == "9":
                        numeral += 'C'
                elif j == 3:
                    if digits[j] == "1":
                        numeral += 'I'
                    elif digits[j] == "2":
                        numeral += 'II'
                    elif digits[j] == "3":
                        numeral += 'III'
                    elif digits[j] == "4":
                        numeral += 'IV'
                    elif digits[j] == "5":
                        numeral += 'V'
                    elif digits[j] == "6":
                        numeral += 'VI'
                    elif digits[j] == "7":
                        numeral += 'VII'
                    elif digits[j] == "8":
                        numeral += 'VIII'
                    elif digits[j] == "9":
                        numeral += 'IX'
    return numeral

for case in cases:
    fnum, snum = case.split('+')
    snum = snum[:-1]

    total = 0
    total += converttoint(fnum)
    total += converttoint(snum)

    print(case + converttonumeral(total))
