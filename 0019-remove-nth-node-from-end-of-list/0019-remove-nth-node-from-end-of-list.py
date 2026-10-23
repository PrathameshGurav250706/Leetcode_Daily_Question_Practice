# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy

        for i in range(n+1):
            fast=fast.next

        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
        # Time complexity: O(L), where L is the length of the linked list. The two-pointer technique traverses the list once after an initial offset, so overall linear time.

        # Space complexity: O(1), aside from the fixed set of pointers and the dummy node, since only a constant number of extra pointers are used.