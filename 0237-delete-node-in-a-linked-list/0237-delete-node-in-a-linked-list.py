class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """

        node.val = node.next.val
        node.next = node.next.next