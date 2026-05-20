"""
788. Rotated Digits

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].



Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Example 2:

Input: n = 1
Output: 0
Example 3:

Input: n = 2
Output: 1


Constraints:

1 <= n <= 104
"""

# time: O(n)
# space: O(n)


class Solution:
    def rotatedDigits(self, n: int) -> int:

        valid_digits_map = {0: 2, 1: 2, 2: 1, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 2, 9: 1}

        counter_good = 0
        tracker = [-1] * (
            n + 1
        )  # init arrays with value of -1, note array[0] is not applicable here

        for i in range(1, n + 1):
            if i < 10:
                # just check the map
                is_good = valid_digits_map[i]
                if is_good == 1:
                    tracker[i] = 1
                    counter_good += 1
                elif is_good == 2:
                    tracker[i] = 2
                else:
                    tracker[i] = valid_digits_map[i]
            else:
                last_digit = i % 10
                all_except_last_digit = i // 10

                is_good_last_digit = valid_digits_map[last_digit]
                is_good_all_except_last_digit = tracker[all_except_last_digit]

                if is_good_last_digit == 1:
                    if is_good_all_except_last_digit == 1:
                        tracker[i] = 1
                        counter_good += 1
                    elif is_good_all_except_last_digit == 2:
                        counter_good += 1
                        tracker[i] = 1

                elif is_good_last_digit == 2:
                    if is_good_all_except_last_digit == 1:
                        tracker[i] = 1
                        counter_good += 1
                    elif is_good_all_except_last_digit == 2:
                        tracker[i] = 2

                else:
                    tracker[i] = 0

        return counter_good
