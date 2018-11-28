'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def create_tree(self):
        root = TreeNode(0)
        p = root
        p.right = TreeNode(1)

        p.left = TreeNode(2)
        return root
    def show_tree(self,root):
        if root!=None:
            print(root.val)
            self.show_tree(root.left)
            self.show_tree(root.right)
        else:
            print('*')


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root !=None:
            tmp = self.Mirror(root.left)
            root.left = self.Mirror(root.right)
            root.right = tmp
        return root
def test_function():
    tree = TreeNode(None)
    root = tree.create_tree()
    tree.show_tree(root)
    solution = Solution()
    root = solution.Mirror(root)
    tree.show_tree(root)
if __name__ == '__main__':
    test_function()
