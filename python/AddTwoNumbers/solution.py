# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Head node of the result linked list
        firstNode = ListNode(0)
        # Current pointer to traverse the result linked list
        current = firstNode
        carry = 0

        while l1 or l2 or carry:
            # Get values from current nodes or  0, if node is None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            totalSum = v1 + v2 + carry
            # Updates carry for next iteration
            carry = totalSum // 10

            # Create new node with the remainder of th totalSum
            current.next = ListNode(totalSum % 10)
            # Moves to next node in the result linked list
            current = current.next

            # Moves to next node if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return firstNode.next
        