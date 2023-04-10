grid = [[5,7,0],[0,3,1],[0,5,0]]
class Solution():
    def checkXMatrix(self, grid):
        r , c = 0, len(grid) - 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == col or row == r and col == c:
                    if grid[row][col] == 0:
                        return False
                else:
                    if grid[row][col] != 0:
                        return False
            r += 1
            c -= 1
        return True
sol = Solution()
print(sol.checkXMatrix(grid))