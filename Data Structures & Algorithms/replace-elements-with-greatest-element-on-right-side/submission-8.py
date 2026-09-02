class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #we move from right to left, setting the last element of our 
        #list to -1 and second to last element as the last element
        #then we run a comparison of the last element with the current element. 
        # the largest value should always overtake as the replacement variable. 
        new_array = [0]*len(arr)
        new_array[-1] = -1
        replacement_var = -1
        for i in range(len(arr)-1, -1, -1):
            new_array[i] = replacement_var
            replacement_var = max(arr[i], replacement_var)
            
        return new_array

            



