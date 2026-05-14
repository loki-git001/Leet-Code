class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_num = max(nums)
        n = len(nums)
        
        if n != max_num + 1:
            return False

        freq = Counter(nums)

        for i in range(1, max_num):
            if freq[i] != 1:
                return False
        
        return freq[max_num] == 2