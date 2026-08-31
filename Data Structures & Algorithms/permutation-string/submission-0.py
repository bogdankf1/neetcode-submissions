class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        s1_count = Counter(s1)
        print('s1_count', s1_count)
        while right <= len(s2):
            s2_substr = s2[left:right + 1]
            s2_substr_count = Counter(s2_substr)
            print('s2_substr_count', s2_substr_count)
            if s1_count == s2_substr_count:
                return True
            else:
                left += 1
                right += 1
        return False