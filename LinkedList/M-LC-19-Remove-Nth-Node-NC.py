## Leetcode link: https://leetcode.com/problems/remove-nth-node-from-end-of-list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        To remove nth node from the left, just need to point (n + 1)th from left to (n - 1)th element from left.
        So to find it, we can either calculate the length of list prior, and traverse upto len - n - 1 element.
        We could also take two pointers, head and dummy, head travels n - 1 nodes.
        Then head and dummy( which is at start ) will start moving until head reaches end.
        This keeps our dummy pointer at n + 1 th node from the left. Now we skip the link. Thats it.

        But there would be edge case where the element to be removed is the first node of list itself.
        So create a arbitrary node that pointsto head so that. arbitrary->1->2->3
        Start the above traversal process with this arbitrary node as start for dummy node, so that in above edge case our dummy pointer will be at 
        this arbitrary node itself and we can remove the first node.
        arb->1->None => arb->None => return arb.next => None
        """
        arb = ListNode(0, head)
        dummy = arb

        for i in range(n - 1):
            head = head.next
        
        while head.next:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next
        return arb.next