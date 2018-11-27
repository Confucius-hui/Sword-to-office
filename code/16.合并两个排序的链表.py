'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        lists = []
        while p1!=None and p2!=None:
            if p1.val > p2.val:
                lists.append(p2.val)
                p2 = p2.next
            else:
                lists.append(p1.val)
                p1 = p1.next
        while p1!=None:
            lists.append(p1.val)
            p1 = p1.next
        while p2!=None:
            lists.append(p2.val)
            p2 = p2.next
        if pHead1 ==None and pHead2 ==None:
            return None
        pHead = ListNode(lists[0])
        p = pHead
        for i in lists[1:]:
            p.next = ListNode(i)
            p = p.next
        return pHead
def test_function():
    head1 = ListNode(0)
    p = head1
    for i in range(1, 6,2):
        node = ListNode(i)
        p.next = node
        p = node


    head2 = ListNode(0)
    p = head2
    for i in range(1, 10,3):
        node = ListNode(i)
        p.next = node
        p = node
    solution = Solution()
    phead = solution.Merge(head1,head2)
    while phead !=None:
        print(phead.val)


if __name__ == '__main__':
    test_function()



