class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }
        stack = []
        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operations[t](a, b)))
            else:
                stack.append(int(t))
        return stack[0]