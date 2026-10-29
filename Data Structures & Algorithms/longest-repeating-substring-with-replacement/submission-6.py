class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_length = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            length = r - l + 1
            while l < r and length - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                length = r - l + 1
            max_length = max(length, max_length)
        return max_length
