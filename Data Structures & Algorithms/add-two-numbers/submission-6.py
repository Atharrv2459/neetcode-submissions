# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        list1 = []
        list2 = []

        while l1:

            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        num1 = 0
        num2 = 0
        for i in range(len(list1)):
            num1 += list1[i] * 10**i
        for i in range(len(list2)):
            num2 += list2[i] * 10**i
        
        sum_num = num1 + num2

        dummy = ListNode(0)
        curr = dummy
        if sum_num == 0:
            return dummy

        while sum_num > 0:
            digit = sum_num % 10
            curr.next = ListNode(digit)
            curr = curr.next
            sum_num //= 10
        return dummy.next

        



        