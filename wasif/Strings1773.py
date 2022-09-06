items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]

ruleKey = "color"
ruleValue = "silver"
ans = 0

indexToCheck = 2
if ruleKey == "type":
    indexToCheck = 0
elif ruleKey == "color":
    indexToCheck = 1

for item in items:
    if item[indexToCheck] == ruleValue:
        ans += 1

print(ans)
