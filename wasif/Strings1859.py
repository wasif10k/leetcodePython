s = "Myself2 Me1 and3 I4"

word1 = s.split(" ")
ans = [None]*len(word1)
answerString = ""

for iword in word1:
    num = int(iword[len(iword)-1])
    ans[num-1] = iword[0:len(iword)-1]

for i in range(0, len(ans)):
    answerString += ans[i]
    if i != len(ans)-1:
        answerString += " "


print (answerString)
