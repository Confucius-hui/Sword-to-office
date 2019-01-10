'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<1:
            return None
        num2 = 0
        num3 = 0
        num5 = 0
        result = [1]
        for i in range(index-1):
            min_value = min(result[num2]*2,result[num3]*3,result[num5]*5)
            result.append(min_value)
            if min_value%2 == 0:
                num2+=1
            if min_value%3 == 0:
                num3+=1
            if min_value%5 == 0:
                num5+=1
        return result

def test_function():
    solution = Solution()
    result = solution.GetUglyNumber_Solution(7)
    print(result)

if __name__ == '__main__':
    test_function()





