class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        newStringAsArray = [None] * len(s);

        for i in range(0, len(newStringAsArray)):
            newStringAsArray[indices[i]] = s[i];

        newString = "";

        for indivChar in newStringAsArray:
            newString += indivChar;

        return newString;