"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

# time: O(n^2)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if (head.next == None):
            return head

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        no_rotate = k % count

        curr = head

        for i in range (0,no_rotate):
            temp_val = 0
            flag = True
            while curr:
                if (flag):
                    temp_val = curr.val
                    curr = curr.next
                    head = curr
                    flag = False
                else:
                    if (curr.next is None):
                        temp_val2 = curr.val
                        curr.val = temp_val
                        curr = ListNode(temp_val2, head)
                        break
                    else:
                        temp_val2 = temp_val
                        temp_val = curr.val
                        curr.val = temp_val2
                        curr = curr.next
            
        return curr

# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Find the new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head          # connect old tail to old head

        return new_head