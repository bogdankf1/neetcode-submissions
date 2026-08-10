class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanums = []
        for l in s:
            if l.isalnum():
                alphanums.append(l.lower())
        new_s = "".join(alphanums)
        left, right = 0, len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True