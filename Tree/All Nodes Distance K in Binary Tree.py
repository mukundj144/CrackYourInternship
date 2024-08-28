# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def markParents(self, root, parent_track, target):
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current.left:
                parent_track[current.left] = current
                queue.append(current.left)
            if current.right:
                parent_track[current.right] = current
                queue.append(current.right)

    def distanceK(self, root, target, k):
        parent_track = {}
        self.markParents(root, parent_track, target)
        
        visited = defaultdict(bool)
        queue = deque([target])
        visited[target] = True
        
        curr_level = 0
        
        while queue:
            if curr_level == k:
                break
            curr_level += 1
            
            for _ in range(len(queue)):
                current = queue.popleft()
                
                if current.left and not visited[current.left]:
                    queue.append(current.left)
                    visited[current.left] = True
                
                if current.right and not visited[current.right]:
                    queue.append(current.right)
                    visited[current.right] = True
                
                if current in parent_track and not visited[parent_track[current]]:
                    queue.append(parent_track[current])
                    visited[parent_track[current]] = True
        
        result = []
        while queue:
            current = queue.popleft()
            result.append(current.val)
        
        return result      