from TreeNode import TreeNode
from typing import Callable


class CraftingTree:
    def __init__(self, item, count, recipe_dict: dict):
        self._root = TreeNode({item: count})
        self._totals = {}
        self._recipe_dict = recipe_dict
        self._add_data(self._root, count, 0)

    def _add_data(self, parent_node: TreeNode, factor: int, depth: int):
        item = tuple(parent_node.data)[0]

        for component in self._recipe_dict[item]["recipe"]:
            number = self._recipe_dict[item]["recipe"][component] * factor

            # Create a new node for each component and add it to the tree
            new_node = TreeNode({component: number})
            parent_node.add_child(new_node)

            # Update the total of each component needed in the whole recipe
            if component not in self._totals:
                self._totals[component] = number
            else:
                self._totals[component] += number

            # Recursively repeat for each component needed in the recipe
            self._add_data(new_node, number, depth + 1)

    def to_string_tree(self, number_formatter: Callable = lambda x: x):
        return self._root.to_string_tree(number_formatter)

    def to_string_list(self, number_formatter: Callable = lambda x: x):
        # Format the total of every component needed in the recipe
        totals = self._totals.items()
        if self._recipe_dict["ordered"]:
            totals = sorted(totals, key=lambda p: self._recipe_dict[p[0]]["order"])
        else:
            totals = sorted(totals)
        totals = map(lambda p: f"{p[0]}: {number_formatter(p[1])}", totals)
        return "\n".join(totals)