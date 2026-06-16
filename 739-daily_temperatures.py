"""
739. Daily Temperatures
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:
O
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

#time: O(n)
#space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        length = len(temperatures)
        output = [0 for _ in range(length)]
        
        for i in range(len(temperatures)-2,-1,-1):
            counter = 0
            curr = i
            while i < len(temperatures)-1:
                counter += 1
                if temperatures[curr] < temperatures[i+1]:
                    output[curr] = counter
                    break
                else:
                    i += 1

        return output
                











