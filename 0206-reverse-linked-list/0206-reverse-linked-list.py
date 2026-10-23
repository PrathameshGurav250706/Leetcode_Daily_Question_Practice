# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        return prev
        # Time complexity: O(n), where n is the number of nodes in the linked list, since we traverse the list once.

        # Space complexity: O(1), excluding the input list, as we only use a few pointers and reverse the links in place.