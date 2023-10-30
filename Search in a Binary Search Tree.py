class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        a = []

        def dfs(node, h):
            if not node:
                return
            if len(a) == h:
                a.append([])

            dfs(node.left, h+1)
            a[h].append(node.val)
            dfs(node.right, h+1)

        dfs(root, 0)

        level_sum = [sum(level) for level in a]
        maximal = max(level_sum)
        
        return 1 + level_sum.index(maximal)
