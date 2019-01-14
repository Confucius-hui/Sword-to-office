'''
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# -*- coding:utf-8 -*-
from functools import reduce
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        dicts = {}
        for i in array:
            dicts[i] = tsum - i
        lists = []
        print(dicts)
        for key in dicts.keys():
            if dicts[key] in array:
                lists.append([key, dicts[key]])
        print(lists)
        if len(lists) == 0:
            return []
        min = lists[0][0]*lists[0][1]
        best = lists[0]
        for i in lists:
            if min > i[0]*i[1]:
                min = i[0]*i[1]
                best = i
        return best

def test_function():
    solution = Solution()
    arrar=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    result = solution.FindNumbersWithSum(arrar,21)
    print(result)


if __name__ == '__main__':
    test_function()


