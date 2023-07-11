from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # tree backtrace
    def _distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if k == 0:
            return [target.val]

        res = []
        def backtrace(n: TreeNode, dist):
            if n is target:
                if n.left:
                    backtrace(n.left, k - 1)
                if n.right:
                    backtrace(n.right, k- 1)
                return k - 1

            if dist == 0:
                res.append(n.val)
                return
            
            if n.left and (back_dist := backtrace(n.left, dist - 1)) is not None:
                if back_dist == 0:
                    res.append(n.val)
                else:
                    if n.right:
                        backtrace(n.right, back_dist - 1)
                    return back_dist - 1
            elif n.right and (back_dist := backtrace(n.right, dist - 1)) is not None:
                if back_dist == 0:
                    res.append(n.val)
                else:
                    if n.left:
                        backtrace(n.left, back_dist - 1)
                    return back_dist - 1

        backtrace(root, -1)
        return res
    
    # graph building
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if k == 0:
            return [target.val]

        graph = defaultdict(list)
        def build_graph(cur: TreeNode, parent: TreeNode):
            if parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)
        res = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])
        while queue:
            cur, distance = queue.popleft()
            if distance == k:
                res.append(cur)
                continue
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return res
