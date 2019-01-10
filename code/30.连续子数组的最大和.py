'''
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array)<1:
            return None
        pos = [array[0]]
        for element in array[1:]: ##前面是正的一定要，负的绝对不要
            pos.append(max(pos[-1]+element,element))
        return max(pos)

def test_function():
    solution = Solution()
    array = [-1,7,8,2]
    result = solution.FindGreatestSumOfSubArray(array)
    print(result)

if __name__ == '__main__':
    test_function()
