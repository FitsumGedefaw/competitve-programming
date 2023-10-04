class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True


class MapSum:

    def __init__(self):
        self.map = {}
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        self.trie.insert(key)

    def sum(self, prefix: str) -> int:
        curr = self.trie.root
        for ch in prefix:
            idx = ord(ch) - 97

            if not curr.children[idx]:
                return 0
            curr = curr.children[idx]

        
        ans = 0
        word = list(prefix)

        def dfs(node):
            nonlocal ans
            if node.isEnd:
                key = "".join(word)
                ans += self.map[key]
            for i in range(len(node.children)):
                if node.children[i]:
                    ch = chr(i + 97)
                    word.append(ch)
                    dfs(node.children[i])
                    word.pop()

        dfs(curr)
        return ans


        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)