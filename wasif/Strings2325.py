dictionary = {}
alphabet = 97
ans = ""

for ikey in key:
    if ikey != ' ' and ikey not in dictionary:
        dictionary[ikey] = chr(alphabet)
        alphabet= (alphabet)+1

for letter in message:
    if letter != ' ':
        ans += dictionary[letter]
    else:
        ans += ' '
