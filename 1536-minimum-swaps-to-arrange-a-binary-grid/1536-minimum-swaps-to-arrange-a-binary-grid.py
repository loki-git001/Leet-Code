class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        maxRight = []
        row_len = len(grid[0])
        for row in grid:
            rightmost = -1
            for i in range(row_len - 1, -1, -1):
                if row[i] == 1:
                    rightmost = i
                    break
            maxRight.append(rightmost)

        n = len(maxRight)
        swaps = 0
        
        for i in range(n):
            if maxRight[i] <= i:
                continue
            
            j = i + 1
            while j < n and maxRight[j] > i:
                j += 1

            if j == n:
                return -1
            
            while j > i:
                maxRight[j], maxRight[j - 1] = maxRight[j - 1], maxRight[j]
                swaps += 1
                j -= 1
        
        return swaps
            