"""
199. Binary Tree Right Side View
Solved
Medium

Topics
conpanies icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# time: O(n)
# space: O(n)
# recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        def helper(node, depth):
            if not node:
                return None
            if depth == len(ans):
                ans.append(node.val)
            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
        helper(root, 0)
        return ans

# time: O(n)
# space: O(n)
# iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = []
        while queue:
            node, depth = queue.popleft()
            if depth == len(ans):
                ans.append(node.val)
            if node.right:
                queue.append((node.right, depth+1))
            if node.left:
                queue.append((node.left, depth+1))
        return ans

  
