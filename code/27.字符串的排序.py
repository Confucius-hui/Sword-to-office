'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''
# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        result = []
        if len(ss) == 0:
            return ss
        res = itertools.permutations(ss)
        for i in res:
            if ''.join(i) not in result:
                result.append(''.join(i))
        return result
    def Permutation1(self,ss):
        if len(ss) <=1:
            return list(set(ss))
        result = set()
        for i in range(len(ss)): ##固定一个字符
            for j in self.Permutation1(ss[:i]+ss[i+1:]):
                result.add(ss[i]+j)
        return sorted(list(result))

def test_function():
    solution = Solution()
    ss= 'aab'
    result = solution.Permutation(ss)
    result1 = solution.Permutation1(ss)
    print(result,'\n',result1)

if __name__ == '__main__':
    test_function()