'''
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0
    def get(self, n):
        self.sum+=n
        n-=1
        return n>0 and self.Sum_Solution(n)
    def Sum_Solution(self,n):
        flag = self.get(n)
        return self.sum

def test_function():
    solution = Solution()
    result = solution.Sum_Solution(10)
    print(result)


if __name__ == '__main__':
    test_function()
