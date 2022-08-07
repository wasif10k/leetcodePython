class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelCount = 0;

        for jewel in jewels:
            for stone in stones:
                if(jewel == stone):
                    jewelCount += 1;

        return jewelCount;