'''
题目描述
输入一个链表，反转链表后，输出新链表的表头。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        Arrys = []
        while pHead.next !=None:
            pHead = pHead.next
            Arrys.append(pHead.val)
        pHead = ListNode(None)
        p = pHead
        for i in range(len(Arrys),0,-1):
            p.next = ListNode(Arrys[i-1])
            p = p.next
        return pHead
def test_function():
    head = ListNode(None)
    p = head
    for i in range(1, 6):
        node = ListNode(i)
        p.next = node
        p = node
    solution = Solution()
    p = solution.ReverseList(head)
    while p.next !=None:
        p = p.next
        print(p.val)
if __name__ == '__main__':
    test_function()
