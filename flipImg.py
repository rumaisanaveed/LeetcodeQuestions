class Solution:
    def flipAndInvertImage(self, image):
        newMatrix = []
        for i in range(len(image)):
            rows = []
            for j in range((len(image[0]) - 1), -1, -1):
                rows.append(image[i][j])
            newMatrix.append(rows)

        for i in range(len(newMatrix)):
            for j in range(len(newMatrix[0])):
                if newMatrix[i][j] == 0:
                    newMatrix[i][j] = 1
                else:
                    newMatrix[i][j] = 0
        return newMatrix
s = Solution()
print(s.flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))

