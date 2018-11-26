'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
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
    result = solution.jumpFloor(10)
    print(result)

if __name__ == '__main__':
    test_function()