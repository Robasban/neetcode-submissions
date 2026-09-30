# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            saveRes = []
            if len(lists) % 2 == 1:
                saveRes.append(lists[-1])
                lists = lists[:-1]
            for i in range(0, len(lists) - 1, 2):
                saveRes.append(self.mergeList(lists[i], lists[i+1]))
            lists = saveRes
        return lists[0] if len(lists) > 0 else None

    def mergeList(self, l1, l2):
        save = prev = ListNode()
        temp = prev.next
        while l1 and l2:
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            prev.next = temp
            temp = temp.next
            prev = prev.next
        
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2

        return save.next
