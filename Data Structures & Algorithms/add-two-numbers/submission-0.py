# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1temp = l1
        l2temp = l2

        prev = None
        save = None

        while l1temp and l2temp:
            temp = ListNode(l1temp.val + l2temp.val)
            if not save:
                save = temp
            if prev:
                prev.next = temp
            prev = temp

            l1temp = l1temp.next
            l2temp = l2temp.next
        
        if l1temp:
            prev.next = l1temp
        elif l2temp:
            prev.next = l2temp
        if not save:
                save = prev

        temp = save

        while temp:
            if temp.val > 9:
                temp.val -= 10
                if temp.next:
                    temp.next.val += 1
                else:
                    temp.next = ListNode(1)
            temp = temp.next

        return save
