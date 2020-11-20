"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, str):
        new_str = ''
        for word in str.split(' '):
            new_str += word[::-1] + ' '

        return new_str


print (Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
print (Solution().reverseWords("She sells sea shells on the sea shore"))
