class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first = abs(heapq.heappop(maxHeap))
            second = abs(heapq.heappop(maxHeap))

            diff = first - second
            if (diff) > 0:
                heapq.heappush(maxHeap, -diff)
        
        return 0 if not maxHeap else -maxHeap[0]