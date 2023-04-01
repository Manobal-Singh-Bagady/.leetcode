#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        mid = len(nums) // 2
        if len(nums) == 0:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[:mid], target)
        if nums[mid] < target:
            res = self.search(nums[mid + 1 :], target)
            if res == -1:
                return -1
            return mid + 1 + res
# @lc code=end

