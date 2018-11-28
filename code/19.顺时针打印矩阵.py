'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        results = []
        if len(matrix)==0:
            return results
        ##获取行数，列数
        m = len(matrix)
        n = len(matrix[0])
        circle = min(m//2,n//2)+1
        lists = []
        for i in range(circle):
            ##左->右
            lists.append(matrix[i][i:i+n-2*i-1])
            ##上到下
            lists.append([a[i+n-2*i-1] for a in matrix[i:i+m-2*i-1]])
            ##右到左
            lists.append(matrix[i+m-2*i-1][i+n-2*i-1:i:-1])
            ##下到上
            lists.append([a[i] for a in matrix[i+m-2*i-1:i:-1]])
        for row in lists:
            for i in row:
                results.append(i)
        return results
    def test(self,matrix):
        result = []
        while matrix:
            result+=matrix.pop(0)
            if matrix and matrix[0]:
                result+=[row.pop() for row in matrix]
            if matrix:
                result+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                result+=[row.pop(0) for row in matrix][::-1]
        return result
def test_function():
    matrixs = []
    for i in range(0,5):
        matrix = []
        for j in range(1,6):
            matrix.append(5*i+j)
        matrixs.append(matrix)
    print(matrixs)
    solution = Solution()
    lists = solution.test([[1],[2],[3],[4],[5]])
    print(lists)

if __name__ == '__main__':
    test_function()