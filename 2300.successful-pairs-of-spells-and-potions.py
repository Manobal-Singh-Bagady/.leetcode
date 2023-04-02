# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
import bisect
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        s_potions = sorted(potions)
        ans = []
        for i in spells:
            ans.append(len(s_potions) -
                       bisect.bisect_left(s_potions, (success+i-1)//i))
        return ans
# @lc code=end


ob = Solution()
print(ob.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
