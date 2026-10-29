class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += '#' + str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            if s[i] == '#' and ord('0') <= ord(s[i + 1]) <= ord('9'):
                j = i + 1
                num = ""
                string = ""
                while s[j] != '#':
                    num += s[j]
                    j += 1
                num = int(num)
                i = j + 1
                while len(string) < num:
                    string += s[i]
                    i += 1
                res.append(string)

        return res