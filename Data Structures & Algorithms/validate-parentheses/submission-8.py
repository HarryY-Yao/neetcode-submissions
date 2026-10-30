class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                peek = stack.pop()
                if ((peek == "(" and c != ")") or (peek == "{" and c != "}") or 
                (peek == "[" and c != "]")):
                    return False

        return len(stack) == 0
