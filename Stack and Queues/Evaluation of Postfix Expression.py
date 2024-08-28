class Solution:
    
    # Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        # Stack to store operands
        st = []

        # Dictionary to map operators to their respective functions
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: b - a,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(b / a)  # Use int() for floor division
        }

        for char in S:
            if char.isdigit():
                # Append integer value of the digit
                st.append(int(char))
            else:
                # Operator encountered
                op1 = st.pop()
                op2 = st.pop()
                # Evaluate using the operator
                res = operators[char](op1, op2)
                st.append(res)
        
        # The final result will be the only element left in the stack
        return st[0]
