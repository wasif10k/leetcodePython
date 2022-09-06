words = ["gin","zen","gig","msg"]


translator = {}
morsecodetable = [".-" ,"-..." ,"-.-." ,"-.." ,"." ,"..-." ,"--." ,"...." ,".." ,".---" ,"-.-" ,".-.." ,"--" ,"-."
                  ,"---" ,".--." ,"--.-" ,".-." ,"..." ,"-" ,"..-" ,"...-" ,".--" ,"-..-" ,"-.--" ,"--.."]
alphabet = 97
answer = ""
x = set()
for letter in morsecodetable:
    translator[chr(alphabet)] = letter
    alphabet += 1

for word in words:
    translatedWord = ""
    for i in word:
        translatedWord += translator[i]
    x.add(translatedWord)

print(len(x))

