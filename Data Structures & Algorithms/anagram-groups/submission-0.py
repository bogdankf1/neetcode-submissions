class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for item in strs:
            sorted_str = "".join(sorted(item))
            groups[sorted_str].append(item)
        
        return list(groups.values())