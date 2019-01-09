'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.head = None
        self.realhead = None
    def Convert(self, pRootOfTree):
        # write code here 中序遍历的非递归算法
        self.Inorder(pRootOfTree)
        return self.realhead
    def Inorder(self,p):
        if not p :
            return None
        self.Inorder(p.left)
        if not self.head:
            self.head = p
            self.realhead = p
        else:
            self.head.right = p
            p.left = self.head
            self.head = p
        self.Convert(p.right)

def testfunction():
    solution  = Solution()
    root = TreeNode(10)
    left = TreeNode(6)
    right = TreeNode(14)
    root.left = left
    root.right = right

    results = solution.Convert(root)
    print(results.val)

if __name__ == '__main__':
    testfunction()