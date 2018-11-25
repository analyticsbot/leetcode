# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, el in enumerate(nums):
            if target-el in nums:
                if i != nums.index(target-el):
                    return i, nums.index(target-el)

# Runtime: 1080 ms, faster than 27.02% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        for num in range(len(nums)):
            val = vals.get(target - nums[num], -10)
            if val >= 0:
                return [val, num]
            else:
                vals[nums[num]] = num

# Runtime: 44 ms, faster than 65.35% of Python3 online submissions for Two Sum.


                