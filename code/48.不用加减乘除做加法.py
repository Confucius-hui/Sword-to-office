'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2!=0:
            tmp = num1^num2 ##直接相加
            num2 = (num1&num2)<<1 ##获取进位
            num1 = tmp
        return num1

def test_function():
    solution = Solution()
    retsult = solution.Add(100,20)
    print(retsult)

if __name__ == '__main__':
    test_function()