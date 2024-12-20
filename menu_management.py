def add_item(menu, item):
    if item not in menu:
        menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Item '{item}' does not exist in the menu.")
    return menu

def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item_name = "Tacos"
initial_menu = add_item(initial_menu, add_item_name)

remove_item_name = "Salad"
initial_menu = remove_item(initial_menu, remove_item_name)

check_item_name = "Pizza"
availability = check_item(initial_menu, check_item_name)

print("Updated menu:", initial_menu)
print("Availability:", availability)
