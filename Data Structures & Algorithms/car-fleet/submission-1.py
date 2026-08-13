class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []
        for p,s in pairs:
            t = (target - p) / s
            if not stack:
                stack.append(t)
            if t <= stack[-1]:
                continue
            if t > stack[-1]:
                stack.append(t)
        return len(stack)