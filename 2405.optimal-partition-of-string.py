# ---------------- MSB's Coding Template ---------------- #
'''
    "ɴᴏ ᴄᴏᴅᴇ ɪꜱ ᴘᴇʀꜰᴇᴄᴛ"
'''

# ---I/O from file---#
from collections import Counter
import sys
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    sys.stderr = open("output.txt", "w")
except:
    pass


# ---------------------- Code Starts Here ----------------------#

#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        d = set()
        count = 1
        for i in s:
            if i in d:
                count += 1
                d.clear()
                d.add(i)
            else:
                d.add(i)
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.partitionString("sssss"))
