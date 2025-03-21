# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        length1=""
        length2=""
        current1=l1
        while current1:
            length1+=str(current1.val)
            current1=current1.next
        current2=l2
        while current2:
            length2+=str(current2.val)
            current2=current2.next
        length3=int(length1[::-1])+int(length2[::-1])
        num3=str(length3)
        a=len(num3)
        dummy = ListNode(0)  
        current = dummy
        for x in num3[::-1]:
            new_node=ListNode(int(x))
            current.next=new_node
            current=current.next

        return dummy.next