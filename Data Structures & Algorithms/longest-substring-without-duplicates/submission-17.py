class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window = set()
        l = 0

        for r in range(0, len(s)):
            if s[r] in window:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                if l < r:
                    l += 1
            window.add(s[r])
            length = r - l + 1
            max_length = max(length, max_length)

        return max_length
            



        