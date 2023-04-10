class Solution:
    def minimumTime(self, N, cur, pos, time):
        output = []
        for i in range(N):
            a = pos[i]
            b = time[i]
            if cur > a:
               c = (cur - a) * b
               output.append(c)
            else:
                c = (a - cur) * b
                output.append(c)
        return min(output)
s = Solution()
print(s.minimumTime(N = 2, cur = 1,
pos = [1, 6],
time = [10, 3]))