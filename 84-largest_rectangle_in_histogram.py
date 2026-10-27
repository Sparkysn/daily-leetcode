"""
84. Largest Rectangle in Histogram
Hard

Topics
conpanies icon
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

# time: O(n)
# space: O(n)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        result = 0
        
        # added in sentinel 0 so that stack will be emptied out at the end
        for i,h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    # right - left - 1
                    width = i - stack[-1] - 1
                else:
                    width = i
                result = max(result, width*height)
            stack.append(i)
        
        return result
