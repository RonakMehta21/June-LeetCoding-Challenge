# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        start = node
        end = node
        start = start.next
        l1=[]
        while start:
            l1.append(start.val)
            start = start.next
        for x in range(len(l1)):
            node.val = l1[x]
            node = node.next
        prev = None
        while end.next!=None:
            prev = end
            end = end.next
        prev.next = None
