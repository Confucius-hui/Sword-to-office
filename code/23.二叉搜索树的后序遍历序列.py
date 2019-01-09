'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence.pop()
        for i in range(len(sequence)):
            if sequence[i] > root:
                right = sequence[i:]
                del sequence[i:]
                left = sequence
                for i in right:
                    if i<root:
                        return False
                for i in left:
                    if i>root:
                        return False
                return self.SquenceOfBST(left) and self.SquenceOfBST(right)
        return True
    def SquenceOfBST(self,sequence):
        if not sequence:
            return True
        if len(sequence) == 1:
            return True
        root = sequence.pop()
        for i in range(len(sequence)):
            if sequence[i] > root:
                right = sequence[i:]
                del sequence[i:]
                left = sequence
                for i in right:
                    if i<root:
                        return False
                for i in left:
                    if i>root:
                        return False
                return self.SquenceOfBST(left) and self.SquenceOfBST(right)
        return self.SquenceOfBST(sequence)
def test_function():
    sequence = [4,6,12,8,16,14,10]
    solution =Solution()
    print(solution.VerifySquenceOfBST(sequence))

if __name__ == '__main__':
    test_function()