class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        j = -1
        for i in range(len(arr)-1, -1, -1):
            k = arr[i]
            arr[i] = j
            j = max(j, k)
        return arr
