class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

       
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        # Time complexity: O(n), where n is the number of nodes in the linked list. The list is traversed twice: once to reach the middle (slow/fast pointers) and once to reverse the second half, plus a final pass to compare halves. Overall linear in n.

        # - Space complexity: O(1) extra space. The algorithm reverses the second half in place and uses a constant number of pointers, with no auxiliary data structures.