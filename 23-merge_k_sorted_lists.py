"""
23. Merge k Sorted Lists
Solved
Hard
Topics
conpanies icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# time: O(nlogn)
# space: O(n)

# brute force (sort at end)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(-1)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for i in sorted(nodes):
            point.next = ListNode(i)
            point = point.next
        return head.next


# time: O(kn)
# space: O(1)

# brute force 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while True:
            min_idx = -1
            for i, node in enumerate(lists):
                if node is not None:
                    if min_idx == -1 or node.val < lists[min_idx].val:
                        min_idx = i
            # all list exhausted
            if min_idx == -1:
                break
            
            tail.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            tail = tail.next
        return dummy.next

# time: O(nlogk)
# space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        heap = []

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next




