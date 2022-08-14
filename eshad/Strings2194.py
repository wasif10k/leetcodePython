class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        startcol = ord(s[0])
        endcol = ord(s[3])
        startrow = ord(s[1])
        endrow = ord(s[4])

        for i in range(startcol, endcol + 1):
            for j in range(startrow, endrow + 1):
                irow = chr(i) + chr(j)
                ans.append(irow)

        return ans