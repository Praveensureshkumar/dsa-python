# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isametree(s,q):
            if not s and not q:
                return True
            if not s or not q:
                return False
            return s.val==q.val and isametree(s.left,q.left) and isametree(s.right,q.right)        
        queue=deque([root])

        while queue:
            node=queue.popleft()
            if isametree(node,subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False