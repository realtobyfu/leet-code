# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
                
        q = deque()
        res = []
        
        if root:
            q.append(root)
        else:
            return []

        while q:
            res.append([n.val for n in q])
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)

        return res
        