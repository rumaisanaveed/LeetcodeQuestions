class Solution:
    def arraySortedOrNot(self, arr, n):
        temp = arr[0]
        for i in range(1,len(arr)):
            if temp <= arr[i]:
                temp = arr[i]
            else:
                return False
        return True
s = Solution()
print(s.arraySortedOrNot([1,2,3,4,5],5))