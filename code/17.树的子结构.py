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
    def isSubtree(self,pRoot1,pRoot2):
        ##2遍历完了，为空
        if pRoot2 == None:
            return True
        ##1便利完了，为空
        if pRoot1 ==None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSubtree(pRoot1.left,pRoot2.left) and self.isSubtree(pRoot1.right,pRoot2.right)
        else:
            return False
    def HasSubtree(self, pRoot1, pRoot2):
        flag = False
        if pRoot1!=None and pRoot2!=None:
            if pRoot1.val == pRoot2.val:
                flag = self.isSubtree(pRoot1,pRoot2)
            if not flag:
                flag = self.isSubtree(pRoot1.left,pRoot2)
            if not flag:
                flag = self.isSubtree(pRoot1.right,pRoot2)
        return flag



