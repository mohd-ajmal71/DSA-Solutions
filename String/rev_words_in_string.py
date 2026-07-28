class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        rev_words = reversed(words)
        return " ".join(rev_words)

