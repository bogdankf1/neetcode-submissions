class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash_map = {}
        for index, num in enumerate(nums):
            if num not in nums_hash_map:
                nums_hash_map[num] = index
            
            second_num = target - num
            if second_num in nums_hash_map:
                second_index = nums_hash_map[second_num]

                if index != second_index:
                    return [second_index, index]
        
        return []