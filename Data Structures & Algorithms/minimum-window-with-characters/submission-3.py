class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {}, {}
        l = have = 0
        need = len(t)
        res = ""

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        for r in range(len(s)):
            if s[r] in count_t:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] <= count_t[s[r]]:
                    have += 1
            
            while have == need:
                if len(res) == 0 or r - l + 1 < len(res):
                    res = s[l:r + 1]
                if s[l] in count_t:
                    window[s[l]] -= 1
                    if window[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
        

        return res


