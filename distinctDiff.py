#Distinct difference
class Solution:
    def getDistinctDifference(self, N, A):
        # code here
        res = []
        for i in range(len(A)):
            left = []
            for j in range(0,i):
                if A[j] not in left:
                    left.append(A[j])
            right = []
            for k in range(i+1,len(A)):
                if A[k] not in right:
                    right.append(A[k])
            diff = len(left) - len(right)
            res.append(diff)
        return res

s = Solution()
print(s.getDistinctDifference(3,[4,3,3]))