class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        add_alt = 0
        for i in gain:
            add_alt = add_alt + i
            if add_alt > max_alt:
                max_alt = add_alt
        return max_alt

