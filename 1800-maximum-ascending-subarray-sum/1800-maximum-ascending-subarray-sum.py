class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        total = nums[0]
        max_sum = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                total += nums[i]
            else:
                max_sum = max(total, max_sum)
                total = nums[i]

        return max(total, max_sum)