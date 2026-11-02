class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = False


    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = self.TrieNode()
                curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(curr, word)
    
    def dfs(self, node, word):
        if len(word) == 0 and node.word:
            return True
        elif len(word) == 0:
            return False

        if word[0] in node.children:
            return self.dfs(node.children[word[0]], word[1:])
        elif word[0] == '.':
            flag = False
            for child in node.children.values():
                flag = flag or self.dfs(child, word[1:])
            return flag
        else:
            return False

