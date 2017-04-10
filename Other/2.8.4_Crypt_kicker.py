#   lntbl is a dictionary whose keys are a length of a word and whose
#   values are the words in library whose length is the length of the key.
#
#

n = int(input())
dcwrds = {}


for i in range(n):
    wrd = input()
    if dcwrds[len(wrd)] not in dcwrds.keys():
        dcwrds[len(wrd)] = wrd
    else:
        dcwrds[len(wrd)].append(wrd)

while True:
    encrptd = input()
    enwrds = {}

    if encrptd == '':
        break
    else:
        encrptd = encrptd.split(' ')

    # Add encrypted words to a length table.
    for wrd in encrptd:
        if enwrds[len(wrd)] not in enwrds.keys():
            enwrds[len(wrd)] = wrd
        else:
            enwrds[len(wrd)].append(wrd)
