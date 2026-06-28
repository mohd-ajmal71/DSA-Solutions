class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = {}
        count = 0
        max = len(candyType) // 2
        for c in candyType:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        types = len(freq)
        if types <= max:
            return types
        else:
            return max