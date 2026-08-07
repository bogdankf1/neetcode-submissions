class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_hash_map = {}
        t_hash_map = {}
        for i in s:
            s_hash_map[i] = s_hash_map.get(i, 0) + 1
        for j in t:
            t_hash_map[j] = t_hash_map.get(j, 0) + 1
        return s_hash_map == t_hash_map