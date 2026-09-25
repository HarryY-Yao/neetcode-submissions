class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = curr_length = max_length = 0
        window = {}

        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = r
            
            else:
                index = window.get(s[r])
                while l <= index:
                    window.pop(s[l])
                    l += 1
                
                window[s[r]] = r
            
            curr_length = r - l + 1
            max_length = max(curr_length, max_length)
        
        return max_length



        