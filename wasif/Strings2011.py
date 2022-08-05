operations =  ["--X","X++","X++"]




x = 0
for op in operations:
    if "++" in op:
        x += 1
    else:
        x -= 1
print (x)

#comment