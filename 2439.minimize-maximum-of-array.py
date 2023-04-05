# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
from itertools import accumulate
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
from math import ceil
class Solution:
    # ----------Solution by MSB----------

    # ==========Brute Force==========
    # def minimizeArrayValue(self, nums: list[int]) -> int:
    # while True:
    #     m = max(nums)
    #     n = nums.index(m)
    #     nums[n]-=1
    #     nums[n-1]+=1
    #     if nums[n-1]>m:
    #         return m

    # ==========Binary Search==========
    # def checkMid(self, arr: list[int], x: int) -> bool:
    #     sum = 0
    #     for i in range(len(arr)):
    #         sum += arr[i]
    #         if sum > (i+1)*x:
    #             return False
    #     return True

    # def minimizeArrayValue(self, nums: list[int]) -> int:
    #     if nums.index(max(nums)) == 0:
    #         return max(nums)
    #     l, r = 0, max(nums)
    #     while l < r:
    #         mid = (l+r)//2
    #         if self.checkMid(nums, mid):
    #             r = mid
    #         else:
    #             l = mid+1
    #     return l

    # ==========Linear Search==========
    def minimizeArrayValue(self, nums: list[int]) -> int:
        return max(ceil(a/(i+1)) for i, a in enumerate(accumulate(nums)))
# @lc code=end


print(Solution().minimizeArrayValue([3, 7, 1, 6]))
