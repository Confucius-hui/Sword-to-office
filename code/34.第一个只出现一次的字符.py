'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.
'''
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        dicts = {}
        if len(s) == 0:
            return -1
        for i in range(len(s)):
            if s[i] in dicts.keys():
                dicts[s[i]][0]+=1
            else:
                dicts.setdefault(s[i],[])
                dicts[s[i]].append(1)
                dicts[s[i]].append(i)
        dicts = sorted(dicts.items(),key=lambda x:x[1][0],reverse=False)
        if dicts[0][1][0] == 1:
            return dicts[0][1][1]
        else:
            return -1
    def FirstNotRepeatingChar1(self,s):
        tmp = list(filter(lambda x:s.count(x)==1,s))
        return -1 if len(tmp)==0 else s.index(tmp[0])

def test_function():
    solution = Solution()
    s = 'aa'
    result = solution.FirstNotRepeatingChar1(s)
    print(result)

if __name__ == '__main__':
    test_function()

