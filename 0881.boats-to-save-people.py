#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        s_people = sorted(people)
        l = 0
        r = len(s_people)-1
        while l <= r:
            if s_people[l] + s_people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        return count
# @lc code=end
