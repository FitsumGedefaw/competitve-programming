class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-count[word], word) for word in count]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
        