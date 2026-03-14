class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
        print(i)
        j = n-1
        while j-1 >= 0 and arr[j] < arr[j-1]:
            j -= 1
        print(j)
        return i==j and i!=0 and j!=n-1
        
