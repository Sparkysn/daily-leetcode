"""
98. Validate Binary Search Tree
Solved
Medium

Topics
conpanies icon
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# time: O(n)
# space: O(n)
# recursive preorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(node, low, high) -> bool:
            if not node:
                return True
            if not low < node.val < high:
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return helper(root, float("-inf"), float("inf"))

# time: O(n)
# space: O(n)
# recursive post-order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(node) -> (bool, float, float):
            # returns (is_valid, min_in_subtree, max_in_subtree)
            if not node:
                return True, float("inf"), float("-inf")
            l_valid, l_min, l_max = helper(node.left)
            r_valid, r_min, r_max = helper(node.right)
            if not (l_valid and r_valid and l_max < node.val < r_min):
                return False, 0, 0
            return True, min(l_min, node.val), max(r_max, node.val)
        return helper(root)[0]





        





        

