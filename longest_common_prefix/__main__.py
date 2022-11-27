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
        prefix_map = {}
        i = 0
        for x in range(len(strs)):
            prefix_map[x] = strs[x][i]
        i + 1
        print(prefix_map)


if __name__ == '__main__':
    solution_class = Solution
    solution_class = Solution.longestCommonPrefix(["flower", "flow", "flight"])
