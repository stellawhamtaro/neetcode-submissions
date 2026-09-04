class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a hashmap 
        mapping = {}
        #create the list we want to return 
        output_list = []
        for i in range(len(nums2)):
            mapping[nums2[i]] = i
        for j in range(len(nums1)):
            output_list.append(mapping[nums1[j]])
        return output_list
