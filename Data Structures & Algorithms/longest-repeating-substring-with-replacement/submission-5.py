class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        count = {}

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            window_length = r - l + 1

            while (l < r and window_length - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
                window_length = r - l + 1

            res = max(window_length, res)
        
        return res
            

