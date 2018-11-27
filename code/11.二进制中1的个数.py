'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n>=0:
            return sum(list(map(lambda x:int(x),bin(n)[2:])))
        else:
            return sum(list(map(lambda x:int(x),bin((2<<31)+n)[2:])))


def test_function():
    solution =Solution()
    result = solution.NumberOf1(-2147483648)
    print(result)
if __name__ == '__main__':
    test_function()