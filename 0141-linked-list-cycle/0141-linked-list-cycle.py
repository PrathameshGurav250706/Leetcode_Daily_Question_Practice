# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow =head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

        # Time complexity: O(n), where n is the number of nodes in the list. In the worst case, both pointers traverse nodes once until a cycle is detected or the end is reached.

        # Space complexity: O(1), since only two pointers are used regardless of list size.