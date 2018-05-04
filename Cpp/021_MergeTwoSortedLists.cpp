/*
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example: 
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *root, *rst;
        rst = new ListNode(-1);
        root = rst;
        
        while(1)
        {
            if(l1 == NULL)
            {
                root->next = l2;
                break;
            }
            if(l2 == NULL)
            {
                root->next = l1;
                break;
            }
            
            if(l1->val < l2->val)
            {
                root = root->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else
            {
                root = root->next = new ListNode(l2->val);
                l2 = l2->next;
            }
        }
        
        return rst->next;
        
    }
};