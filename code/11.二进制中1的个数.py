'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        lists = []
        if n>=0:
            while n !=0:
                lists.append(n % 2)
                n = n//2
            return sum(lists)
        else:
            n = -n
            tmp = n
            while n!=0:
                lists.append(n%2)
                n = n//2
            length = len(lists)
            n = (2<<(length+1))-tmp
            lists = []
            while n!=0:
                lists.append(n%2)
                n = n//2
            return sum(lists)+1


def test_function():
    solution =Solution()
    result = solution.NumberOf1(-2147483648)
    print(result)
if __name__ == '__main__':
    test_function()