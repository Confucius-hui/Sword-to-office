'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        dicts = {}
        for element in array:
            if element in dicts.keys():
                dicts[element] +=1
            else:
                dicts[element] = 1
        print(dicts)
        lists = []
        for key,value in zip(dicts.keys(),dicts.values()):
            if value%2:
                lists.append(key)
        return lists

def test_function():
    solution = Solution()
    result = solution.FindNumsAppearOnce([1,1,2,2,3,4])
    print(result)

if __name__ == '__main__':
    test_function()

