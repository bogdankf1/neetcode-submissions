class Solution:
    def find_rotation_offset(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return left
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = self.find_rotation_offset(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            real = (mid + offset) % n
            if nums[real] > target:
                right = mid -1
            elif nums[real] < target:
                left = mid + 1
            else:
                return real
        return -1
