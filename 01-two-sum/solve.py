class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if m.has_key(x):
                return [m[x], i]
            m[nums[i]] = i
        return [-1, -1]
