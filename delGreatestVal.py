class Solution():
    def deleteGreatestValue(self,grid):
        newGrid = grid.copy()
        for i in range(len(grid)):
            grid[i] = []
        lst = []
        while newGrid != grid:
            tempList = []
            for row in newGrid:
                maxV = max(row)
                idx = row.index(maxV)
                value = row.pop(idx)
                tempList.append(value)
            lst.append(max(tempList))
        return sum(lst)
s = Solution()
print(s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))


