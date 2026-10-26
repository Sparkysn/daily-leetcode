"""
42. Trapping Rain Water
Solved
Hard
Topics
conpanies icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# time: O(n)
# space: O(n)

class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        result = 0 
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                # index right wall - index left wall - 1
                width = i - stack[-1] - 1 
                # min of height of right wall vs height of left wall - bottom
                bound = min(h, height[stack[-1]]) - bottom 
                result += width*bound
            stack.append(i)
        return result

# time: O(n)
# space: O(1)

class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        result = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                result += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                result += right_max - height[r]
                r -= 1
        return result

