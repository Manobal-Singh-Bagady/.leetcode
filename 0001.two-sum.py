#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
# @lc code=end
