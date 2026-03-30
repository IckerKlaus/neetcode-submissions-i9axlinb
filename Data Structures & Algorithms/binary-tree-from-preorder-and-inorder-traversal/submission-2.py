# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # hashmap de valor -> índice en inorder
        mapping = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # puntero global sobre preorder

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # tomar el siguiente valor de preorder como raíz
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # encontrar su posición en inorder
            mid = mapping[root_val]

            # construir subárbol izquierdo y derecho
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)
