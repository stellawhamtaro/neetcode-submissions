class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalidset = {2,3,4,5,7}
        string_n = str(n)
        for i in range(len(string_n)):
            if int(string_n[i]) in invalidset:
                return False
        valid_dict={}
        valid_dict["0"] = "0"
        valid_dict["1"]="1"
        valid_dict["6"]="9"
        valid_dict["8"]="8"
        valid_dict["9"]="6"
        rotated_n = ""
        for i in range(len(string_n)-1, -1, -1):
            rotated_n += valid_dict[string_n[i]]
        return rotated_n != string_n