class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def findDuplicate(self, nums):
        # Create a set to store seen values
        seen = set()
        
        # Create a dummy node
        dummy = ListNode(0)
        current = dummy
        
        for num in nums:
            # Check if the value is already seen
            if num in seen:
                return num
            
            # Add the value to the seen set
            seen.add(num)
            
            # Create a new node with the current value
            current.next = ListNode(num)
            current = current.next
        
        # If no duplicates found, return -1 or any indicator of choice
        return -1  # Or raise an exception or handle differently as per requirement