class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0 
        for i in range(len(arr)-1):
            maxNum = 0
            for j in range(i+1, len(arr)):
                maxNum = max(arr[j],maxNum)
            arr[i] = maxNum
        arr[-1] = -1
        return arr

