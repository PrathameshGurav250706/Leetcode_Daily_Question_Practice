# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # if head is None or head.next  is None:
        #     return head

        # for i in range(k):
        #     curr=head
        #     while curr.next.next:
        #         curr=curr.next
        #     after=curr.next
        #     curr.next=None
        #     after.next=head
        #     head=after
        # return head
        if head is None or head.next  is None:
            return head
        
        tail=head
        length=1
        while tail.next:
            tail=tail.next
            length+=1
        
        k=k%length
        if k==0:
            return head
        
        tail.next=head

        steps=length-k

        curr=head
        for i in range(steps -1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        return new_head
        # Time complexity: O(n), where n is the number of nodes in the linked list. You traverse the list once to find the tail and length, then potentially traverse up to length - k steps to reach the new tail.

        # Space complexity: O(1), aside from a few pointers, since the rotation is done in place with a constant amount of extra space.