class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre_arr = [0] * 26
        window_size = 0
        max_window = 0
        left = 0
        for i in range(len(s)):
            idx = ord(s[i]) - 65
            fre_arr[idx] += 1
            max_fre = max(fre_arr)
            window_size = (i + 1) - left

            if window_size - max_fre > k:

                while (window_size - max_fre > k):
                    idx = ord(s[left]) - 65
                    fre_arr[idx] -= 1
                    window_size -= 1
                    max_fre = max(fre_arr)
                    left += 1

            if window_size - max_fre <= k:
                if window_size > max_window:
                    max_window = window_size

        return max_window


