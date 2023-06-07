from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # def _find_depth(self, head: TreeNode):
    #     if not head:
    #         return 0
    #     max_depth = 1
    #     d = deque([(1, head)])
    #     while len(d) > 0:
    #         depth, n = d.pop()
    #         if depth > max_depth:
    #             max_depth = depth
    #         if n.left:
    #             d.append((depth + 1, n.left))
    #         if n.right:
    #             d.append((depth + 1, n.right))
    #     return max_depth

    # def serialize(self, head: TreeNode):
    #     max_depth = self._find_depth(head)
    #     if max_depth == 0:
    #         return ""

    #     a = []
    #     d = deque([(1, head)])
    #     while len(d) > 0:
    #         depth, n = d.popleft()
    #         if not n:
    #             a.append("n")
    #             if depth < max_depth:
    #                 d.append((depth + 1, None))
    #                 d.append((depth + 1, None))
    #         else:
    #             a.append(str(n.val))
    #             if depth < max_depth:
    #                 d.append((depth + 1, n.left))
    #                 d.append((depth + 1, n.right))
    #     return ",".join(a)

    def serialize(self, head: TreeNode):
        a = []

        def collect(n: TreeNode):
            if n:
                a.append(str(n.val))
                collect(n.left)
                collect(n.right)
            else:
                a.append("n")

        collect(head)

        return " ".join(a)

    def deserialize(self, data: str):
        lst = iter(data.split())

        def build():
            return (
                TreeNode(int(v), build(), build()) if (v := next(lst)) != "n" else None
            )

        return build()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root = None
# root.right.right.left = TreeNode(71)
# root.left.left.left.left = TreeNode(8)
# root.right.right.right.right = TreeNode(9)

# root = None
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
print(ser.serialize(root))
print(ser.serialize(deser.deserialize(ser.serialize(root))))
# ans = deser.deserialize(ser.serialize(root))
