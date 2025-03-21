# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode()
        dummy.next=head
        current=dummy.next
        length=0
        while current:
            current=current.next
            length+=1
        current=dummy.next
        if length==1:
            return current.next
        if length==n:
            return current.next
        for x in range(length-n-1):
            current=current.next
        temp=current.next
        current.next=temp.next
        return dummy.next








        