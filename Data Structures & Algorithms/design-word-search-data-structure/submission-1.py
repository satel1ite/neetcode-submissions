class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, index):
            for i in range(index, len(word)):
                char = word[i]
                if char != '.':
                    if char in node.children:
                        node = node.children[char]

                    else:
                        return False
                else:
                    for child in node.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
            return node.is_word
        return dfs(curr, 0)




