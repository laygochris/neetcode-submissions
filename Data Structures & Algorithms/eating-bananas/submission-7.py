class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res
        minTime = 0

        while l <= r:
            k = (l + r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                r = k - 1
                res = min(res, k)
                
            else:
                l = k + 1
                print(l, r)

        return res

            
            
