def average(nums):
    return sum(nums) / len(nums)

def brute_force(nums, k):
    for i in range(len(nums)):
        tmp_nums = nums[:i] + nums[i+1 :]
        avg = average(tmp_nums)
        if avg == k:
            return True
    return False

class Solution:
    def solve(self, nums, k):
        # Brute force it
        # return brute_force(nums, k)
        diff = (k * (len(nums)-1) - sum(nums)) * -1
        return diff in nums