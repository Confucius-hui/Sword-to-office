'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot2 and pRoot1:
            flag1 = False
            flag2 = False
            if pRoot1.val == pRoot2.val:
                flag1 = self.HasSubtree(pRoot1.left,pRoot2.left) & self.HasSubtree(pRoot1.right,pRoot2.right)
            flag2 =  self.HasSubtree(pRoot1.left,pRoot2) | self.HasSubtree(pRoot1.right,pRoot2)
            return flag1 | flag2
        elif  pRoot2==None:
            return True
        else:
            return False


