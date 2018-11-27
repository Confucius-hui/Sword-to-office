'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail1(self, head, k):
        p = head
        count = 0
        q = head
        while p.next != None:
            p = p.next
            count +=1
            if count == k:
                q = head
            if q.val != None:
                q = q.next
        return q.val
    def FindKthTotail2(self,head,k):
        length = len(head)
        if length<k:
            return None
        return head[-k]


def test_function():
    head = ListNode(None)
    p = head
    for i in range(1,10):
        node = ListNode(i)
        p.next = node
        p = node
    solution = Solution()
    result1 = solution.FindKthToTail1(head,19)
    head2 = [1,2,3,5,7]
    result2 = solution.FindKthTotail2(head2,5)
    print(result1,result2)

if __name__ == '__main__':
    test_function()