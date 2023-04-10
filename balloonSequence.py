class Solution:
    def maxInstance(self, s):
        # code here
        b = s.count('b')
        a = s.count('a')
        l = s.count('l')
        o = s.count('o')
        n = s.count('n')
        if b == 0 or a == 0 or l == 0 or o == 0 or n == 0:
            return 0
        else:
            minSingleChar = min(b, min(a, n))
            print(minSingleChar)
            minDoubleChar = min(l, o)
            minDoubleChar //= 2
            print(minDoubleChar)
            return min(minSingleChar, minDoubleChar)
s = Solution()
print(s.maxInstance("bnlbllanmbaamnmobbanablboolonlol"))

