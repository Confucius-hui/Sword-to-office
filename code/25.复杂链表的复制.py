'''
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        head = pHead
        p = head
        ##在原链表上插入复制节点
        while head:
            node = RandomListNode(head.label)
            node.next = head.next
            head.next = node
            node.random = head.random
            head = node.next
        p = pHead
        pclone = pHead.next
        pcloneHead = pHead.next
        #拆分链表
        while p:
            p.next = p.next.next
            if pclone.next:
                pclone.next = pclone.next.next
            p = p.next
            pclone = pclone.next
        return pcloneHead
def test_function():
    solution = Solution()
    pHead = RandomListNode(0)
    p1 = RandomListNode(1)
    p2 = RandomListNode(2)
    p3 = RandomListNode(3)
    pHead.next = p1
    pHead.random = p2
    p1.next = p2
    p1.random = p3
    p2.next = p3
    p2.random = p1
    p3.next = None
    p3.random = p2
    result = solution.Clone(pHead)
    while result:
        print(result.label)
        result = result.next

if __name__ == '__main__':
    test_function()
