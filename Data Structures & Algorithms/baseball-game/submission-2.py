class Solution:
    def calPoints(self, operations: List[str]) -> int:
        FinalList = []
        FinalSum =0
        for i in range(len(operations)):
            if operations[i] == '+':
                FinalList.append(FinalList[-1]+FinalList[-2])
            elif operations[i] == 'D':
                FinalList.append(FinalList[-1]*2)
            elif operations[i] == 'C':
                FinalList.pop()
            else:
                FinalList.append(int(operations[i]))
        for j in range(len(FinalList)):
            FinalSum += FinalList[j]
        return FinalSum

        