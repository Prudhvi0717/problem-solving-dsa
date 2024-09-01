## link: https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Since we know how to merge two sorted linked lists, we just need to merge all of them.
    We reduce them to one sorted list in merge sort fashion.
    So the time complexity will be, we process all the nodes O(n) * logk times where k is no.of lists.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        mergedLists = []

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeSortedLists(l1, l2))
            lists = mergedLists
        
        return lists[0]


    def mergeSortedLists(self, l1, l2):
        res = ListNode()
        dummy = res

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1: dummy.next = l1
        if l2: dummy.next = l2

        return res.next