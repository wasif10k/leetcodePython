class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total_jewels = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    total_jewels += 1;
        return total_jewels
