# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        def reverse(node, count):
            if not node:
                return None

            prev, curr = None, node
            while curr and count > 0:
                count -= 1
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # FIX 1: Return 'prev' (the new head of this reversed segment)
            return prev

        if not head:
            return None

        # Track the overall result head and the tail of the previously processed group
        new_head = None
        prev_group_tail = None

        trav = head
        revHead = head
        count = 0

        while trav:
            count += 1

            if count == k:
                count = 0
                temp = trav.next  # Start of the next unprocessed group

                # 'tail' will be the old head (e.g. node 1)
                tail = revHead

                # Reverse the k nodes; 'new_sub_head' will be the node at 'trav' (e.g. node 3)
                new_sub_head = reverse(revHead, k)

                # Save the overall head of the result list on the first group reversal
                if not new_head:
                    new_head = new_sub_head

                # Connect previous group's tail to current reversed group's head
                if prev_group_tail:
                    prev_group_tail.next = new_sub_head

                # Link current group's tail (node 1) to the start of next group (node 4)
                tail.next = temp

                # Set up pointers for the next iteration
                prev_group_tail = tail
                revHead = temp
                trav = temp

                # FIX 2: Continue so we don't execute 'trav = trav.next' below!
                continue

            trav = trav.next

        # If 'new_head' was never set (k > list length), return original head
        return new_head if new_head else head