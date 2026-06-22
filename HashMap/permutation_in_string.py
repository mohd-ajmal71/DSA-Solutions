class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fre_arr1 = [0] * 26
        fre_arr2 = [0] * 26

        for ch in s1:
            idx = ord(ch) - 97
            fre_arr1[idx] += 1
        size = len(s1)

        for i in range(len(s2) - size + 1):
            fre_arr2 = [0] * 26
            for j in range(i, i + size):
                idx = ord(s2[j]) - 97
                fre_arr2[idx] += 1

            if fre_arr1 == fre_arr2:
                return True

        return False







