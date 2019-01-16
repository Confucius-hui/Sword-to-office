'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。
'''
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        length = len(A)
        B = []
        for i in range(length):
            element = self.calculate(A[:i])*self.calculate(A[i+1:])
            B.append(element)
        return B

    def calculate(self,nums):
        result = 1
        for num in nums:
            result*=num
        return result

def test_function():
    solution = Solution()
    A = [1,2,3]
    result = solution.multiply(A)
    print(result)

if __name__ == '__main__':
    test_function()