# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = self.get_val(l1) + self.get_val(l2)
        result = [int(val) for val in str(result)]

        for index in range(len(result)):
            if index == 0:
                previous = ListNode(result[index], next=None)
            else:
                previous = ListNode(result[index], next=previous)
        return previous

    def get_val(self, linked):
        res = ""
        while linked.next is not None:
            res = str(linked.val) + res
            linked = linked.next
        return int(str(linked.val) + res)

