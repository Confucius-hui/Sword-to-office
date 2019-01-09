'''
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        lists = []
        if root :
            lists.append(self.path(root,[],[]))
            print(lists)
        result = []
        for i in lists[0]:
            if sum(i) == expectNumber:
                result.append(i)
        print(result)
        return result
    def path(self,root,sequence,all):
        lists = []+sequence
        if root:
            lists.append(root.val)
            if  root.left:
                self.path(root.left,lists,all)
            if  root.right:
                self.path(root.right,lists,all)
        all.append(lists)
        return all

    def FindPath1(self,root,expectNumber):
        if not root:
            return []
        if root and root.val==expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath1(root.left,expectNumber-root.val)
        right = self.FindPath1(root.right,expectNumber-root.val)
        for i in left+right:
            res.append([root.val]+i)
        return res

def test_function():
    root = TreeNode(10)
    left = TreeNode(5)
    right = TreeNode(12)
    root.left = left
    root.right = right
    left.left = TreeNode(4)
    left.right = TreeNode(7)
    solution = Solution()
    result = solution.FindPath1(root,15)
    print(result)

if __name__ == '__main__':
    test_function()