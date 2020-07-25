class Solution(object):
    def twoSum(self, nums, target):
        for i in tuple(reversed(range(len(nums)))):
            kk = target - nums.pop()
            if kk in nums:
                return i, nums.index(kk)



f = Solution()
print(f.twoSum([3, 2, 4], 6))

