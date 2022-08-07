class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [None] * len(s)
        for i in range(0, len(indices)):
            x = indices[i]
            output[x] = s[i]
        output_string = ""
        for character in output:
            output_string += character
        return output_string;
