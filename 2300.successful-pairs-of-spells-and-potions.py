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
        # s_potions = sorted(potions)
        # return [(len(s_potions) - bisect.bisect_left(s_potions, (success)//i) if success % i == 0 else len(s_potions) - bisect.bisect_right(s_potions, (success)//i)) for i in spells]

        s_potions = sorted(potions)
        ans = []
        for i in spells:
            if success % i == 0:
                neg = bisect.bisect_left(s_potions, (success)//i)
            else:
                neg = bisect.bisect_right(s_potions, (success)//i)
            ans.append(len(s_potions) - neg)
        return ans
# @lc code=end


ob = Solution()
print(ob.successfulPairs([3, 1, 2], [8, 5, 8], 16))
