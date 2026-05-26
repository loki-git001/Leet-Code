class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr_len = len(flowerbed)

        if arr_len == 1:
            return flowerbed[0] + n <= 1

        count = 0

        if flowerbed[0] + flowerbed[1] == 0:
            count = 1 
            i = 2
        else :
            i = 1

        while i < arr_len-1:
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1

        count += 1 if arr_len > 2 and flowerbed[-1] + flowerbed[-2] == 0 else 0

        print(count)
        return count >= n


        

