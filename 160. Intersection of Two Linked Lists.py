# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA == None or headB == None:
            return None

        p_A = headA
        p_B = headB

        # Counter to keep track of linked list switching
        swap_A = 0
        swap_B = 0

        while (True):
            # Scanning through Linked list A and switching to B when reaching the end

            # When there is an intersection
            if p_A == p_B:
                return p_A

            if p_A != None:
                p_A = p_A.next
            else:
                p_A = headB
                swap_A = swap_A + 1

            # Scanning through Linked list B and switching to A when reaching the end
            if p_B != None:
                p_B = p_B.next
            else:
                p_B = headA
                swap_B = swap_B + 1

            # Condition when no intersection happens
            if swap_A == 2 and swap_B == 2:
                return None