class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        maxSpaces = 0;

        for indivWord in sentences:
            currentSpaces = 0;
            for indivChar in indivWord:
                if (indivChar == ' '):
                    currentSpaces += 1;
            if (currentSpaces > maxSpaces):
                maxSpaces = currentSpaces;

        return maxSpaces + 1;
