class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def to_string_tree(self, num_format=lambda x: x):
        def append_text_recursive(parent: TreeNode, depth):
            item, count = tuple(parent.data.items())[0]
            tree_repr.append(f"{depth * '    '}{item} - {num_format(count)}")
            for child in parent.children:
                append_text_recursive(child, depth + 1)
        tree_repr = []
        append_text_recursive(self, 0)
        return "\n".join(tree_repr)