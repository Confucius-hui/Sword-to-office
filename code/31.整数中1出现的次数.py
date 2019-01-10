'''
从1到n中出现1的次数
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        counts = 0
        for i in range(1,n+1):
            counts+=self.Judge1(i)
        return counts
    def Judge1(self,num):
        count = 0
        while num>0:
            if num%10 == 1:
                count+=1
            num = num//10
        return count


def test_function():
    solution = Solution()
    result = solution.NumberOf1Between1AndN_Solution(13)
    print(result)


if __name__ == '__main__':
    test_function()