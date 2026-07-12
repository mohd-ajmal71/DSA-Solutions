class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))
        rank = {}

        for i, num in enumerate(unique, 1):
            rank[num] = i

        return [rank[num] for num in arr]


