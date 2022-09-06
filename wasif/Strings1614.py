s = "(1+(2*3)+((8)/4))+1"

parenthesis = 0
maxParenthesis = 0

for p in s:
    if p == "(":
        parenthesis += 1
    elif p == ")":
        parenthesis -= 1
    else:
        if parenthesis > maxParenthesis:
            maxParenthesis = parenthesis

print (maxParenthesis)