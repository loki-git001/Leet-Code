class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()

        max_el = nums[-1]
        if len(nums) != max_el + 1 or nums[-1] != nums[-2]:
            return False
        
        for i in range(max_el - 1):
            if nums[i] != i + 1:
                return False
        return True