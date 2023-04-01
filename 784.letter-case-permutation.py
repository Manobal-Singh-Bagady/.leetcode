#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = ['']
        for ch in s:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res
# @lc code=end
