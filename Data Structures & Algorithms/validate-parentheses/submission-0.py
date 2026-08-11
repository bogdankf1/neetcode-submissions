class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}": "{", ")": "(", "]": "["}
        stack = []
        for c in s:
            print('c', c)
            print('stack', stack)
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack