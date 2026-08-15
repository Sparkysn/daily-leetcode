"""
19. Remove Nth Node From End of List
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        length = 0
        first = head
        
        # get the length of linklist
        while first is not None:
            length += 1
            first = first.next

        # for edge case whereby node is linklist length is 1 or 2
        first = dummy
        length = length - n
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next
            
        
