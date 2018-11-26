'''
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        if  self.stack1:
            for i in self.stack1[::-1]:
                self.stack2.append(i)
                del self.stack1[-1]
            element = self.stack2[-1]
            del self.stack2[-1]
            for i in self.stack2[::-1]:
                self.stack1.append(i)
                del self.stack2[-1]
        else:
            return None
        return element
def test_function():
    solution = Solution()
    for i in range(4):
        solution.push(i)
    element = solution.pop()
    print(element)
    print(solution.stack1)
    element = solution.pop()
    print(element)
    print(solution.stack1)

if __name__ == '__main__':
    test_function()
