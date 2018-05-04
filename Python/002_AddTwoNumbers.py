## 002 Add two numbers
## You are given two non-empty linked lists 
## representing two non-negative integers. 
## The digits are stored in reverse order and 
## each of their nodes contain a single digit. 
## Add the two numbers and return it as a linked 
## list.You may assume the two numbers do not 
## contain any leading zero, except the number 0 itself.

"""
Example 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = n = ListNode(0)
        sum = l1.val + l2.val
        l3.val = sum%10
        sum = sum//10
        l1 = l1.next
        l2 = l2.next
        while sum != 0 or l2 != None or l1 != None:
            sum = sum + (l1 != None and l1.val or 0) + (l2 != None and l2.val or 0)
            l3.next = ListNode(sum%10)
            l3 = l3.next
            l1 = (l1 != None and l1.next or None)
            l2 = (l2 != None and l2.next or None)
            sum = sum//10
        
        return n
