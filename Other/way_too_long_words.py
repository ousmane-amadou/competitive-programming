n = int(input())
words = []

for i in range(n):
    word = raw_input()
    words.append(word)

for wrd in words:
    print wrd[0]+""+str(len(wrd)-2)+""+word[-1]
