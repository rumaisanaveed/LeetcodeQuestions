class Solution():
    def luckyNumbers(self,matrix):
        luckyNums = []
        for row in matrix:
            minV = min(row)
            idx = row.index(minV)
            colValues = []
            for r in range(len(matrix)):
                colValues.append(matrix[r][idx])
            maxV = max(colValues)
            if maxV == minV:
                luckyNums.append(minV)
        return luckyNums
s = Solution()
print(s.luckyNumbers(matrix = [[7,8],[1,2]]))
