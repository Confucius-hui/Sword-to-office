# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        length = len(s)
        if length == 0:
            return ''
        texts = s.split(' ')
        lists = []
        for i in range(len(texts)-1,-1,-1):
            lists.append(texts[i])
            lists.append(' ')
        del lists[-1]
        return ''.join(lists)


def test_function():
    solution = Solution()
    s = 'I am a student.'
    result = solution.ReverseSentence(s)
    print(result)


if __name__ == '__main__':
    test_function()
