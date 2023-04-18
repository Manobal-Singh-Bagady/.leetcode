#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        if len(s) == 0 or len(s) == 1:
            return True
        else:
            for i in range(len(s)//2):
                if s[i] != s[-i-1]:
                    return False
            return True
# @lc code=end
