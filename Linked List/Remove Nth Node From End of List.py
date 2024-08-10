class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = second = head 

        # Move the first pointer ahead by n steps
        for i in range(n):
            first = first.next

        # Handle the case where the node to be removed is the head of the list
        if not first:
            return head.next

        # Move both pointers till the first pointer reaches the end
        while first.next:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return head 