# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
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
            

        