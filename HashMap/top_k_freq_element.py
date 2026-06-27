class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = k
        ans = []
        freq = {}
        for digit in nums:
            if digit in freq:
                freq[digit] += 1
            else:
                freq[digit] = 1

        sorted_item = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for num, f in sorted_item:
            if count > 0:
                ans.append(num)
                count -= 1
            else:
                break
        return ans






