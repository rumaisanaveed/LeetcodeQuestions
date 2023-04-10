import copy

class Solution:
    def transpose(self,matrix,n):
        a = copy.deepcopy(matrix)
        c = 0
        for i in a:
            r = i
            for j in range(len(a)):
                matrix[j][c] = r[j]
            c += 1
        return matrix
s = Solution()
print(s.transpose([[1,2,3],
             [4,5,6],
             [7,8,9]],3))
