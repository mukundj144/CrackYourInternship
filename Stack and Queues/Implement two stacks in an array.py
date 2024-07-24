
class TwoStacks:
    def __init__(self):
        self.res1 = []
        self.res2 = []

    # Function to push an integer into stack 1
    def push1(self, x: int) -> None:
        self.res1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x: int) -> None:
        self.res2.append(x)

    # Function to remove an element from the top of stack 1
    def pop1(self) -> int:
        if self.res1:
            return self.res1.pop()
        return -1  # Return None if the stack is empty

    # Function to remove an element from the top of stack 2
    def pop2(self) -> int:
        if self.res2:
            return self.res2.pop()
        return -1  # Return None if the stack is empty
