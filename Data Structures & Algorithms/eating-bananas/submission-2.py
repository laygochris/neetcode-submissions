class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            hours = 0
            k =( l + r) // 2
            print(l, " + ", r, "// 2 = ", k)

            
            for p in piles:
                print(p, k)
                hours += math.ceil(p / k)

            print(hours)
            if hours <= h:
                print(hours, res, k)
                res = min(res, k)
                # if it is fast enough, try and see if we can go slower
                r = k - 1
            else:
                # not fast enough, need to increase k
                l = k + 1
        
        return res

