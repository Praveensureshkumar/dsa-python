# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index={value:idx for idx,value in enumerate(inorder)}

        self.pos=0

        def find(left,right):
            if left>right:
                return None
            root_val=preorder[self.pos]
            self.pos+=1
            root=TreeNode(root_val)

            root.left=find(left, inorder_index[root_val]-1)
            root.right=find(inorder_index[root_val]+1,right)

            return root
        
        return find(0,len(inorder) - 1)

        