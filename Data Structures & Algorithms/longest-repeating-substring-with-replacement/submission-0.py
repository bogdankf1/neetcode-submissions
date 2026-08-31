class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left, result = 0, 0

        for right, c in enumerate(s):
            count[c] += 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result