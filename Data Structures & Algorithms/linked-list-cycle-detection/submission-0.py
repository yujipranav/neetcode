# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

     ##Hashset SC: O(n), TC: O(n)

        # seen = set()
        # cur = head
        # while cur:
        #     if cur in seen:
        #         return True

        #     else:
        #         seen.add(cur)

        #     cur = cur.next

        # return False

    #Fast and Slow pointer method SC: O(1) TC: O(n)
        fptr = head
        sptr = head

        while fptr and fptr.next:
            sptr = sptr.next
            fptr = fptr.next.next
            if sptr == fptr:
                return True
        
        return False


        