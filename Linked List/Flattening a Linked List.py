'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None
'''
class Solution:
    def merge(self, a, b):
        # Dummy node to help with merging
        dummy = Node(0)
        current = dummy

        while a and b:
            if a.data < b.data:
                current.bottom = a
                a = a.bottom
            else:
                current.bottom = b
                b = b.bottom
            current = current.bottom

        # Attach the remaining nodes
        if a:
            current.bottom = a
        elif b:
            current.bottom = b

        return dummy.bottom

    def flatten(self, root):
        if root is None:
            return root

        # Initialize the result with the head of the first list
        result = root

        # Iterate through each list in the `next` pointers
        current = root.next
        while current:
            result = self.merge(result, current)
            current = current.next

        return result