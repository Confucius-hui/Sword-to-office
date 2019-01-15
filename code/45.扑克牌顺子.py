# -*- coding:utf-8 -*-

class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False
        kings = numbers.count(0)
        numbers = sorted(numbers)
        for i,number in enumerate(numbers[:-1]):
            if number!=0:
                if numbers[i] == numbers[i+1]:
                    return False
                if numbers[i+1]-numbers[i]-1 > kings:
                    return False
                kings-=(numbers[i+1]-numbers[i]-1)
                if kings<0:
                    return False
        return True

def test_function():
    solution = Solution()
    flag = solution.IsContinuous([0,0,1,3,5])
    print(flag)

if __name__ == '__main__':
    test_function()

