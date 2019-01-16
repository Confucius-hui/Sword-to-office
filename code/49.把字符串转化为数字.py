'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
'''


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if self.is_number(s):
            return int(s)
        else:
            return 0
    def is_number(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

def test_function():
    solution = Solution()
    s = '1a33'
    result = solution.StrToInt(s)
    print(result)

if __name__ == '__main__':
    test_function()