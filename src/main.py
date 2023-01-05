from food.chicken_menu import chicken_menu
from food.burger_menu import burger_menu
import inquirer


# -------------------  Important Variables -------------------
menu_options = ["Chicken Menu", "Burger Menu", "Sushi Menu"]
chicken_options = chicken_menu.show_menu()
burger_options = burger_menu.show_menu()
# sushi_options = sushi_menu.show_menu() # Need to implement
# ------------------------------------------------------------


# Create single function to show user all food options from menu they select
# Create single function to show user description of food they select from food options

def main():

    print("\nWelcome to the Linked-List Restaurant!\n")

    menu_questions = [
    inquirer.List('menu',
                    message=f"What menu would you like to see?",
                    choices=menu_options,
                    ),
    ]
    menu_response = inquirer.prompt(menu_questions)

    view_menu_options(menu_response["menu"])


def view_menu_options(menu_response):

    if menu_response == "Chicken Menu":
        menu_options = chicken_options
    elif menu_response == "Burger Menu":
        menu_options = burger_options
    else:
        menu_options = "not implemented yet"

    menu_options_questions = [
    inquirer.List('menu_options',
                    message=f"What from the {menu_response} would you like to find out more about?",
                    choices=menu_options,
                    ),
    ]
    menu_options_response = inquirer.prompt(menu_options_questions)


if __name__ == "__main__":
    main()
