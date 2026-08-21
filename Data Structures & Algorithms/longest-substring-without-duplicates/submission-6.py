class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_count = 0
        for right, c in enumerate(s):
            if c not in seen:
                seen.add(c)
            else:
                while c in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(c)
            
            max_count = max(max_count, right-left+1)
        
        return max_count
            