class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if s == '+':
                    stack.append(op2 + op1)
                elif s == '-':
                    stack.append(op2 - op1)
                elif s == '*':
                    stack.append(op2 * op1)
                elif s == '/':
                    stack.append(int(op2 / op1))

        return stack[0]
