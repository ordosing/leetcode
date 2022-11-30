"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1
"""

class Solution():
    def isPalindrome(x):
        """
        Solution 1: Slower
        """

        reversed_num = 0
        number = x
        if reversed_num < 0:
            return False
        else:
            while number > 0:
                reversed_num = (reversed_num * 10) + number % 10
                number = number//10
            return x == reversed_num


    def isPalindrome(x):
        """
        Solution 2: Fastest
        """

        if x < 0:
            return False
        return str(x) == str(x)[::-1]

if __name__ == '__main__':
    solution_class = Solution
    solution = Solution.isPalindrome(121)
    print(solution)
    solution = Solution.isPalindrome(-121)
    print(solution)
    solution = Solution.isPalindrome(10)
    print(solution)