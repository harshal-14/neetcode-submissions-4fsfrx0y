# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # approach:
        # find the mid
        tortoise, hare = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        # 1st part keep as is
        # 2nd part of list reverse it
        second = tortoise.next
        tortoise.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next   # save next
            curr.next = prev  # reverse the pointer
            prev = curr       # advance prev
            curr = nxt        # advance curr
        
        # merge the 2 elements of the list one by one
        first, second = head, prev
        while second:
            # save next pointers
            tmp1 = first.next
            tmp2 = second.next

            first.next = second    # 1 → 4
            second.next = tmp1     # 4 → 2

            # advance both pointers
            first = tmp1
            second = tmp2

        # how to find the mid