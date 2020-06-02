# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            l = []
            l.append(root)
            while len(l)!=0:
                curr = l.pop(0)
                curr.left,curr.right = curr.right,curr.left
                if curr.left!=None:
                    l.append(curr.left)
                if curr.right!=None:
                    l.append(curr.right)
        return root
        '''
        # Recursive Solution
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right = root.right,root.left
        return root
        '''
