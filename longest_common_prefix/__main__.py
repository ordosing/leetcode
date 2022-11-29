"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution():
    def longestCommonPrefix(strs: List[str]) -> str:
        list_len = len(strs)
        # If the list is 1 element, return
        if list_len == 1:
            return strs[0]
        shortest_string = min(strs, key=len)
        common = ''
        # Set outer loop counter
        i = 0
        # Only iterate over the length of the shortest string
        while i < len(shortest_string):
            # Get the letter of in position i of the first string in list
            letter = strs[0][i]
            # Set inner loop counter
            x = 1
            while x < list_len:
                # Get the letter in the string
                compare = strs[x][i]
                # Compare the letter with the same index of the previous string
                if compare != letter:
                    return common
                x = x + 1
            common += letter
            i = i + 1
        return common


if __name__ == '__main__':
    solution_class = Solution
    solution = Solution.longestCommonPrefix(["flower", "flow", "flight"])
    print(solution)
    solution = Solution.longestCommonPrefix(["dog", "racecar", "car"])
    print(solution)
    solution = Solution.longestCommonPrefix(["sheeple", "sheeps", "sheeping"])
    print(solution)
