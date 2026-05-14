class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) != max(nums) + 1:
            return False

        nums.sort()
        for i in range(1, max(nums)):
            try:
                if nums[i-1] != i:
                    return False
            except IndexError:
                return False
        return nums[-1] == max(nums) and nums[-2] == max(nums)