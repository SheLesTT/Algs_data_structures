class BinaryTree:
    def __init__(self, val, level=0):
        self.val = val
        self.left = None
        self.right = None
        self.level = level

    def add_node(self, val):

        if val == self.val:
            return None
        if val < self.val:
            if self.left == None:
                self.left = BinaryTree(val, self.level + 1)
                return self.left
            else:
                return self.left.add_node(val)

        else:
            if self.right == None:
                self.right = BinaryTree(val, self.level + 1)
                return self.right
            else:
                return self.right.add_node(val)

    def leaves(self):

        elements = []
        if self.left:
            elements += self.left.leaves()
        if self.right:
            elements += self.right.leaves()
        if not self.left and not self.right:
            elements.append(self.val)
        return elements

    def dfs(self):
        elements = []

        if self.left:
            elements += self.left.dfs()
        elements.append(self.level)
        if self.right:
            elements += self.right.dfs()
        return elements

    # def tree_height(self):
    #     if self.left
    def balanced(self):
        left = right = 0
        if self.left:
            left self.left.balanced()
        if self.right:
            return self.right.balanced()
        return True
    def reverse_sort(self):
        elements = []
        if self.right:
            elements += self.right.reverse_sort()
        elements.append(self.val)
        if self.left:
            elements += self.left.reverse_sort()
        return elements


def build_tree_get_level(nodes):
    tree = BinaryTree(nodes[0], 1)
    for val in nodes[1:]:
        tree.add_node(val)
    return tree


nodes = list(map(int, input().split()))
tree = build_tree_get_level(nodes[:-1])
print(*tree.leaves())
