'''
统计一个数字在排序数组中出现的次数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)


def test_function():
    solution = Solution()
    data = [1,2,2,2,2,3,4]
    result = solution.GetNumberOfK(data,2)
    print(result)

if __name__ == '__main__':
    test_function()