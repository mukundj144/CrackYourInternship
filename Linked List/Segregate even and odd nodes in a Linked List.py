# User function Template for Python3

# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        if not head or not head.next:
            return head

        even_head = even_tail = None
        odd_head = odd_tail = None
        current = head

        while current:
            next_node = current.next
            if current.data % 2 == 0:
                if even_head is None:
                    even_head = even_tail = current
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if odd_head is None:
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next
            current.next = None
            current = next_node

        if even_tail:
            even_tail.next = odd_head
        return even_head if even_head else odd_head
