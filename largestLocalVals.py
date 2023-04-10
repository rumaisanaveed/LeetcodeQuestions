class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        ans = []
        for i in range(n - 2):
            res = []
            for j in range(n - 2):
                k = []
                k.append(grid[i][j])
                k.append(grid[i][j + 1])
                k.append(grid[i][j + 2])
                k.append(grid[i + 1][j])
                k.append(grid[i + 1][j + 1])
                k.append(grid[i + 1][j + 2])
                k.append(grid[i + 2][j])
                k.append(grid[i + 2][j + 1])
                k.append(grid[i + 2][j + 2])
                m = max(k)
                res.append(m)
            ans.append(res)

        return ans
s = Solution()
print(s.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
