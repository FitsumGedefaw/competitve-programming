class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def trieNode(c):
            return {'count': 1}
        trie = {}
        for word in words:
            currentTrie = trie
            for c in word:
                if c not in currentTrie:
                    currentTrie[c] = trieNode(c)
                else:
                    currentTrie[c]['count'] += 1
                currentTrie = currentTrie[c]

        scores = []

        for word in words:
            currentScore = 0
            currentTrie = trie
            for c in word:
                currentScore += currentTrie[c]['count']
                currentTrie = currentTrie[c]
            scores.append(currentScore)
        return scores