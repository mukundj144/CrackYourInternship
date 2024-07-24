'''
class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
'''
class Solution:
    def multiply_two_lists(self, first, second):
        mod = 10**9+7
        # Helper function to convert linked list to integer
        def list_to_int(node):
            num = 0
            while node:
                num = (num * 10 + node.data)%mod
                node = node.next
            return num

        # Convert both linked lists to integers
        num1 = list_to_int(first)
        num2 = list_to_int(second)
        
        # Multiply the integers
        product = (num1 * num2)%mod
        
        return product
