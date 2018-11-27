'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        arr1 = []
        arr2 = []
        for i in array:
            if i%2 == 1:
                arr1.append(i)
            else:
                arr2.append(i)
        return arr1+arr2

def test_function():
    solution = Solution()
    array = [1,2,3,4,5,6,7]
    result = solution.reOrderArray(array)
    print(result)

if __name__ == '__main__':
    test_function()