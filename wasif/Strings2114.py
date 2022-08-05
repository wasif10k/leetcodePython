class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_value = 0
        for indiv_sentence in sentences:
            spaces = 0
            for character in indiv_sentence:
                if character == ' ':
                    spaces += 1;
            if spaces > max_value:
                max_value = spaces;
        return max_value + 1;

