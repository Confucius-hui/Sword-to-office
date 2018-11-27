'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        return base**exponent

def test_function():
    solution = Solution()
    result = solution.Power(2,-3)
    print(result)

if __name__ == '__main__':
    test_function()