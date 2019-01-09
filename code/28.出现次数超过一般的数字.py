'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        n = len(numbers)
        if n == 0:
            return 0
        dicts = {}
        for number in numbers:
            if number in dicts.keys():
                dicts[number]+=1
            else:
                dicts[number]=1
        dicts = sorted(dicts.items(),key=lambda item:item[1],reverse=True)
        if dicts[0][1] > n/2:
            return dicts[0][0]
        else:
            return 0

def test_function():
    solution = Solution()
    numbers = [1,2,3,2,2,2,5,4,2]
    solution.MoreThanHalfNum_Solution(numbers)

if __name__ == '__main__':
    test_function()