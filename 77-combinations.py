"""
77. Combinations
Medium
Topics
conpanies icon
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""

# time: O(k · C(n, k))
# time: O(k)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTrack(curr, first_num):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            need = k - len(curr)
            remain = n - first_num + 1
            available = remain - need
            print(need,remain,available)

            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backTrack(curr, num + 1)
                curr.pop()
        ans = []
        backTrack([],1)
        return ans
