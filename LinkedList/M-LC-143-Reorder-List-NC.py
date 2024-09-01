## Leetcode link: https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        The intuition is to:
        To reorder list in such a way that elements from end (right to left) are placed at the alternate positions
        from left to right. Split the list into two parts and reverse the second part. So that now we can traverse
        the first part from left to right like 1->2->3 and second part from right to left i.e 4<-5<-6.
        While traversing we merge both.

        Steps to implement:
        1. Find the middle of the linked list.
        2. Split the list into two halfs
           Eg: 1->2->3->4->5 => 1->2->3 4->5
        2. Reverse the second half of the linked list.
           Eg: 1->2->3 4->5 => 1->2->3 4<-5
        3. Now place two pointer at start and end, merge both the lists.
        """

        ## find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ## split the list into two
        second = slow.next
        slow.next = None
        prev = None

        ## reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        ## merge both parts
        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        return head
