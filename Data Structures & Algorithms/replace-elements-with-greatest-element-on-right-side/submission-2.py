class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        rightMaxList = [None]*len(arr)
        for j in range(len(arr)-1,-1,-1):
            rightMaxList[j] = rightMax
            rightMax = max(rightMax, arr[j])     
        return rightMaxList
            
