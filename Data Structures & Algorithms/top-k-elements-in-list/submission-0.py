class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash_map = {}
        result = []
        for num in nums:
            nums_hash_map[num] = nums_hash_map.get(num, 0) + 1
        pairs = nums_hash_map.items()
        sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse = True)
        keys = [pair[0] for pair in sorted_pairs[:k]]
        return keys