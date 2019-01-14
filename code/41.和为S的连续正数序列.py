'''
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
# -*- coding:utf-8 -*-
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        lists = []
        for i in range(1,tsum//2+1):
            tmp = (-1+math.sqrt(1-4*(i-i**2-2*tsum)))/2
            if tmp%1 == 0:
                lists.append([i for i in range(i,int(tmp)+1)])
        return lists

def test_function():
    solution = Solution()
    result = solution.FindContinuousSequence(3)
    print(result)

if __name__ == '__main__':
    test_function()



