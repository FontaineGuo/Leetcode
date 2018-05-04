## 021 Merge Two Sorted Lists

## Merge two sorted linked lists 
## and return it as a new list. The 
## new list should be made by splicing 
## together the nodes of the first two lists.

'''
Example: 
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None :
            return l2
        elif l2 == None:
            return l1
        
        l3 = n = ListNode(0)

        if l1.val < l2.val:
            l3.val = l1.val
            l1 = l1.next
        else:
            l3.val = l2.val
            l2 = l2.next
   
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        
        if l1 == None:
            l3.next = l2
        elif l2 == None:
            l3.next = l1
        
        return n