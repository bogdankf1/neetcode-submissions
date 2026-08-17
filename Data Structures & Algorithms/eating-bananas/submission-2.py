class Solution:
    def hours(self, piles, k):
        return sum(math.ceil(p / k) for p in piles)
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if self.hours(piles, mid) <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer