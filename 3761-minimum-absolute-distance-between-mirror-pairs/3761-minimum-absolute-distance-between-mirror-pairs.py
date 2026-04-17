class Solution:
    def rev_num(self, num):
        rev = 0
        while num > 0:
            rev = (rev * 10) + num % 10
            num //= 10
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        hash_map = {}
        dis = float("inf")
        for i in range(len(nums)):
            if nums[i] in hash_map:
                dis = min(dis, abs(i - hash_map[nums[i]]))
                if dis == 1:
                    return dis
            hash_map[self.rev_num(nums[i])] = i

        return dis if dis != float("inf") else -1
