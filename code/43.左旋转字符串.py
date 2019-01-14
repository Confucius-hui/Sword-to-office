'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if len(s) ==0:
            return ''
        if len(s) == 1:
            return s
        flag = n%len(s)
        for i in range(flag):
            s = list(s)
            tmp = s[0]
            del s[0]
            s.append(tmp)
        return ''.join(s)

def test_function():
    solution = Solution()
    s = 'abcXYZdef'
    result = solution.LeftRotateString(s,100)
    print(result)


if __name__ == '__main__':
    test_function()





