'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        a = 1
        b = 1
        for i in range(2,number+1):
            s = a+b
            a = b
            b = s
        return s
def test_function():
    solution = Solution()
    result = solution.rectCover(10)
    print(result)

if __name__ == '__main__':
    test_function()