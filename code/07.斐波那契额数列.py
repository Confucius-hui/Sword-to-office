# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci1(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci1(n-1)+self.Fibonacci1(n-2)
    def Fibonacci2(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for i in range(2,n+1):
            s = a+b
            a = b
            b = s
        return s


def test_function():
    solution = Solution()
    result1 = solution.Fibonacci1(10)
    result2 = solution.Fibonacci2(10)
    print(result1,result2)

if __name__ == '__main__':
    test_function()