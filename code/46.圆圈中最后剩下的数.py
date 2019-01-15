# -*- coding:utf-8 -*-
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.pre = None
class Solution:
    def LastRemaining_Solution(self, n, m):
        circles = []
        for i in range(n):
            circles.append(i)
        if n == 0:
            return None
        i = 0
        flag = 0
        while len(circles)!=1:
            i = (m+i-1)%len(circles)
            circles.pop(i)
        return circles




def test_function():
    soltion = Solution()
    result = soltion.LastRemaining_Solution(4,2)
    print(result)
if __name__ == '__main__':
    test_function()


