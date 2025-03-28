import json
from CraftingTree import CraftingTree
from notation import int_to_scietific_notation


# Returns the name of a recipe item given from the user if the
# item is found in recipes_list
def prompt_recipe_item_name_from_user(recipes_list: dict) -> tuple[str, int]:
    def capitalize_words(x: str) -> str:
        words_split = x.split(" ")
        words_split_capitalized = [word.capitalize() for word in words_split]
        return " ".join(words_split_capitalized)

    # Get item's name
    message = "What item are you crafting?\n>> "
    item_name: str = capitalize_words(input(message).strip())

    # Verify item is a real recipe
    if item_name not in recipes_list:
        print(f"Error: \"{item_name}\" is not in the given recipe table\n")
        return "", -1

    return item_name, 0


#
def prompt_item_count_from_user(itemName: str) -> tuple[int, int]:
    # Set errmessage for specifc error
    def print_not_positive_integer_error_message(c):
        print(f"Error: {c} is not a positive integer\n")

    # Get count from user
    message = f"How many {itemName} are you making?\n>> "
    user_input: str = input(message).strip()
    if not user_input:
        item_count = 0
    elif not user_input.isdigit():
        print_not_positive_integer_error_message(user_input)
        return 0, -1
    else:
        item_count = float(user_input)

    # Verify item_count is entered as an integer
    if item_count % 1 != 0:
        print_not_positive_integer_error_message(item_count)
        return 0, -1

    # Verify item_count is entered as a positive number
    if item_count % 1 < 0:
        print_not_positive_integer_error_message(item_count)
        return 0, -1

    return int(item_count), 0


def prompt_recipe_from_user(recipes_list: dict) -> tuple[str, int]:
    while True:
        item_name, err, = prompt_recipe_item_name_from_user(recipes_list)
        if err:
            continue

        item_count, err = prompt_item_count_from_user(item_name)
        if err:
            continue

        break

    return item_name, item_count


def main():
    with open("../resource/recipe.json", 'r') as recipes_file:
        recipes: dict = json.load(recipes_file)
    # tree = CraftingTree("Computer6", 10, recipes)
    # print(tree.asList(MCInotiation.scientific))

    # Get item and count from user
    item, count = prompt_recipe_from_user(recipes)
    print()

    # Create tree from item and count
    tree = CraftingTree(item, count, recipes)

    # Print the tree
    print(f"List for {count} {item}:\n{tree.to_string_list(int_to_scietific_notation)}\n")
    print(f"Tree for {count} {item}:\n{tree.to_string_tree(int_to_scietific_notation)}\n")


if __name__ == "__main__":
    main()
