"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

class Solution:
    def romanToInt(s: str) -> int:
        numeral_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Return value
        response = 0
        # Length of string passed
        s_len = len(s)
        # Iterator
        i = 0
        while i < s_len:
            # Get the index of the current (c) character.
            c_index = list(numeral_dict.keys()).index(s[i])
            # Get the int value for the next character.
            c_value = numeral_dict[s[i]]
            # If not the last character in the string.
            if i < s_len-1:
                # Get the index of the next (n) character.
                n_index = list(numeral_dict.keys()).index(s[i+1])
                # Get the int value of the next character.
                n_value = numeral_dict[s[i+1]]
                # Get the difference between the indices.
                index_diff = n_index - c_index
                # If the indice differnce is 1 or 2, subtract int value of the current character
                # from the int value of the next character then add it to the response value.
                if 0 < index_diff <= 2:
                    response += (n_value - c_value)
                    # Increase the iterator by 2 since the c and n characters represented one integer.
                    i += 2
                else:
                    # Otherwise, just add the current character's int value to the response.
                    response += c_value
                    i += 1
            else:
                # Add the last number to the reponse.
                response += c_value
                i += 1
        return response

if __name__ == '__main__':
    solution_class = Solution
    solution = Solution.romanToInt('III')
    print(solution)
    solution = Solution.romanToInt('LVIII')
    print(solution)
    solution = Solution.romanToInt('XXXIII')
    print(solution)
    solution = Solution.romanToInt('MDCLXXXIII')
    print(solution)
