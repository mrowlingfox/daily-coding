class Solution:
    def solve(self, nums):
        nums = set(nums)
        result = -1
        for num in nums:
            if num > result and num * -1 in nums:
                result = num
        return result