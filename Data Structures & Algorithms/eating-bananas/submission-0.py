class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            time = 0

            for pile in piles:
                time += (pile + mid - 1) // mid

            if time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res