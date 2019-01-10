'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self,numbers):
        if len(numbers) == 0:
            return ""
        result = self.PrintMinNumber1(numbers)
        return int(result[0])
    def PrintMinNumber1(self, numbers):
        if len(numbers) == 1:
            return [numbers[0]]
        result = set()
        for i in range(len(numbers)):
            for j in self.PrintMinNumber1(numbers[:i]+numbers[i+1:]):
                result.add(str(numbers[i])+str(j))
        return sorted(result)

def test_function():
    solution = Solution()
    numbers = [3,32,321]
    result = solution.PrintMinNumber(numbers)
    print(result)

if __name__ == '__main__':
    test_function()