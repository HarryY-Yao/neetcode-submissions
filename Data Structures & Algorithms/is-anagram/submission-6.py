class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in count_s:
                count_s[s[i]] = 1
            else:
                count_s[s[i]] += 1

            if t[i] not in count_t:
                count_t[t[i]] = 1
            else:
                count_t[t[i]] += 1 

        return count_s == count_t