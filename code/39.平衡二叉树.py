'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        else:
            left = self.TreeDepth(pRoot.left)
            right = self.TreeDepth(pRoot.right)
            if abs(left-right)>1:
                return False
            else:
                flag1 = self.IsBalanced_Solution(pRoot.left)
                flag2 = self.IsBalanced_Solution(pRoot.right)
                return flag1 and flag2
    def TreeDepth(self,pRoot):
        if pRoot == None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1

def test_function():
    root = TreeNode(1)
    p2 = TreeNode(2)
    p3 = TreeNode(3)
    p4 = TreeNode(4)
    p5 = TreeNode(5)
    p6 = TreeNode(6)
    p7 = TreeNode(7)
    root.left = p2
    root.right = p3
    p2.left = p4
    p2.right = p5
    p3.left = p6
    p3.right = p7
    solution = Solution()
    flag = solution.IsBalanced_Solution(root)
    print(flag)

if __name__ == '__main__':
    test_function()
