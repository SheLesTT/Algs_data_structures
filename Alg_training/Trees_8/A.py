
class BinaryTree:
    def __init__(self, val, level=0):
        self.val = val
        self.left = None
        self.right = None
        self.level = level

    def add_node(self, val):
        if val == self.val:
            return
        if val < self.val:
            if self.left == None:
                self.left = BinaryTree(val, self.level + 1)
            else:
                self.left.add_node(val)
        else:
            if self.right == None:
                self.right = BinaryTree(val, self.level + 1)
            else:
                self.right.add_node(val)


    def dfs(self):
        elements = []

        if self.left:
            elements += self.left.dfs()
        elements.append(self.level)
        if self.right:
            elements += self.right.dfs()
        return elements
def build_tree_get_level(nodes):
    tree = BinaryTree(nodes[0], 1)
    for val in nodes[1:]:
        tree.add_node(val)
    return tree

nodes = list(map(int, input().split()))
tree = build_tree_get_level(nodes[:-1])
print(max(tree.dfs()))