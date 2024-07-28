class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operation = '+'
        s += '+'  # Add a dummy '+' operator at the end to handle the last number

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char in '+-*/':
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_num))  # Truncate toward zero

                operation = char
                current_num = 0

        return sum(stack)
