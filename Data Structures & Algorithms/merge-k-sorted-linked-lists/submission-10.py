# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(p, q):
            tail = dummy = ListNode()

            while tail:
                if not p:
                    tail.next = q
                    break
                if not q:
                    tail.next = p
                    break

                if p.val > q.val:
                    tail.next = q
                    q = q.next
                else:
                    tail.next = p
                    p = p.next
                tail = tail.next
            
            return dummy.next

        
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(merge(l1, l2))
            lists = mergedList
        
        return lists[0]
            
            
            

