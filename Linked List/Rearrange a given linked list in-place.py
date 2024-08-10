class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        if not head or not head.next or not head.next.next:
            return

        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    

        # Reverse the second half of the linked list
        second=slow.next
        prev=slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        first,second = head, prev 
        
        while second:
            holder1, holder2 = first.next, second.next
            first.next = second
            second.next = holder1
            first, second = holder1, holder2
