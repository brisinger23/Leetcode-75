
class Solution:
    ans1 = []
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.ans1 = []
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                if root.left == None and root.right == None:
                    self.ans1.append(root.val)
                inorderTraversal(root.right)

        inorderTraversal(root1)
        inorderTraversal(root2)

        if self.ans1[:(len(self.ans1)//2)] == self.ans1[(len(self.ans1)//2):] :
            return True
        else:
            return False
        
