# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            # recursive calls begin here --> newHead will always be the tail
            # once the base case is reached
            newHead = self.reverseList(head.next)
            # head.next.next = newHead ==> newHead -> head
            # reversing the list
            head.next.next = head
        # breaks previous chains and also sets the head-> next to none
        # once we reach the end of the list
        head.next = None

        return newHead