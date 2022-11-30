"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution():
    def isValid(s):
        matchDict = {'(': ')', '[': ']', '{': '}'}
        rightPart = set([')', ']', '}'])
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif matchDict.get(stack[len(stack) - 1]) == c:
                stack.pop()
            elif c in rightPart:
                return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    solution_class = Solution
    solution = Solution.isValid("()")
    print(solution)
    solution = Solution.isValid("()[]{}")
    print(solution)
    solution = Solution.isValid("(]")
    print(solution)