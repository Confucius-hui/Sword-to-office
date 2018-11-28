'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
    def push(self, node):
        self.stack.append(node)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        if self.stack:
            _min = self.stack[0]
            for i in self.stack:
                if i<=_min:
                    _min = i
            return  _min
        return None

