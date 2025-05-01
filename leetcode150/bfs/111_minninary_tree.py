# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque()
        if not root:
            return 0
        queue.append((root,1))
        while(queue):
            (cur,depth) = queue.popleft()
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                queue.append((cur.left,depth + 1))
            if cur.right:
                queue.append((cur.right,depth + 1))
        return depth