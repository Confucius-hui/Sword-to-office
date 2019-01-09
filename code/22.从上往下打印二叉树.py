'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        values = []
        nodes = []
        if root:
            values.append(root.val)
            nodes.append(root.left)
            nodes.append(root.right)
        while nodes:
            node = nodes.pop(0)
            if node:
                values.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
        return values
