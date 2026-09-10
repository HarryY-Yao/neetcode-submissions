class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoding = "#" + str(len(s)) + "#" + s
            encoded += encoding
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == "#" and (ord('1') <= ord(s[i + 1]) <= ord('9')):
                if int(s[i + 1]) != 0:
                    num = s[i + 1]
                    j = i+2
                    
                    while (s[j] != "#"):
                        num += s[j]
                        j += 1
                    
                    length = int(num)
                    j += 1

                    word = ""
                    while len(word) < length:
                        word += s[j]
                        j += 1
                    decoded.append(word)
                    i = j
            else:
                decoded.append("")
                i += 3

        return decoded

