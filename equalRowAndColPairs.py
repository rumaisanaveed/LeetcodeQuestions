class Solution:
    def equalPairs(self, grid):
        pairs = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ro = []
                for c in range(len(grid)):
                    ro.append(grid[row][c])
                co = []
                for r in range(len(grid[0])):
                    co.append(grid[r][col])
                if ro == co:
                    pairs += 1
        return pairs
s = Solution()
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
