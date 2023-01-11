from food.chicken_menu import chicken_menu
from food.burger_menu import burger_menu
from food.sushi_menu import sushi_menu
import inquirer


# ----------------------------------------------------------------------------------------------------------------------
#                                           ---  Important Variables ---
menu_options = ["Chicken Menu", "Burger Menu", "Sushi Menu"]
chicken_options = {"food_menu": chicken_menu.show_menu(), "food_descriptions": chicken_menu.show_food_descriptions()}
burger_options = {"food_menu": burger_menu.show_menu(), "food_descriptions": burger_menu.show_food_descriptions()}
sushi_options = {"food_menu": sushi_menu.show_menu(), "food_descriptions": sushi_menu.show_food_descriptions()}
# ----------------------------------------------------------------------------------------------------------------------

# TODO:
# 1. Cleanup view_food_descriptions()
# 2. Add Ascii art upon program launch
# 3. Add emojis to different menus, chicken, burger, sushi

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
        food_options = chicken_options["food_menu"]
        food_descriptions = chicken_options["food_descriptions"]
    elif menu_response == "Burger Menu":
        food_options = burger_options["food_menu"]
        food_descriptions = burger_options["food_descriptions"]
    else:
        food_options = sushi_options["food_menu"]
        food_descriptions = sushi_options["food_descriptions"]

    
    menu_options_questions = [
    inquirer.List('food',
                    message=f"What from the {menu_response} would you like to find out more about?",
                    choices=food_options,
                    ),
    ]
    menu_options_response = inquirer.prompt(menu_options_questions)

    view_food_description(menu_options_response["food"], food_descriptions)


def view_food_description(menu_options_response, food_descriptions):

    print(menu_options_response)
    print(food_descriptions[menu_options_response])

if __name__ == "__main__":
    main()
