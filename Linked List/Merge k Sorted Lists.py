import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged_list = []
        
        # Extract values from the linked lists into a single list for merging
        for l_list in lists:
            while l_list:
                merged_list.append(l_list.val)
                l_list = l_list.next
        
        # Sort the merged list using quicksort
        self.quick_sort(merged_list, 0, len(merged_list) - 1)
        
        # Create a new linked list from the sorted merged list
        dummy = ListNode()
        current = dummy
        for val in merged_list:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next

    def quick_sort(self, a, first, last):
        if first < last:
            #choosing the random pivot for better optimization
            pivot_index = random.randint(first, last)
            a[first], a[pivot_index] = a[pivot_index], a[first]
            
            pivot = a[first]
            i = first
            j = last

            while i < j:
                while i < last and a[i] <= pivot:
                    i += 1
                while j > first and a[j] > pivot:
                    j -= 1
                if i < j:
                    a[i], a[j] = a[j], a[i]

            a[first], a[j] = a[j], a[first]

            self.quick_sort(a, first, j - 1)
            self.quick_sort(a, j + 1, last)