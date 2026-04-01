class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return all(ch.isupper() for ch in word) or all(ch.islower() for ch in word) or (word[0].isupper() and all(ch.islower() for ch in word[1:]))
