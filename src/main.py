from food.burger_menu import burger_menu, burger_menu_emoji
from food.chicken_menu import chicken_menu, chicken_menu_emoji
from food.sushi_menu import sushi_menu, sushi_menu_emoji
from utils.restaurant_title import title
import inquirer


# ----------------------------------------------------------------------------------------------------------------------
#                                           ---  Important Variables ---
menu_options = [f"Burger Menu {burger_menu_emoji}", f"Chicken Menu {chicken_menu_emoji}", f"Sushi Menu {sushi_menu_emoji}"]
chicken_options = {"food_menu": chicken_menu.show_menu(), "food_descriptions": chicken_menu.show_food_descriptions()}
burger_options = {"food_menu": burger_menu.show_menu(), "food_descriptions": burger_menu.show_food_descriptions()}
sushi_options = {"food_menu": sushi_menu.show_menu(), "food_descriptions": sushi_menu.show_food_descriptions()}
# ----------------------------------------------------------------------------------------------------------------------


# TODO: 
# 1: After a user views the final food description, see if they want to view the menu options again

def main():

    title()
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

    if menu_response == f"Burger Menu {burger_menu_emoji}":
        food_options = burger_options["food_menu"]
        food_descriptions = burger_options["food_descriptions"]
        food_emoji = burger_menu_emoji
    elif menu_response == f"Chicken Menu {chicken_menu_emoji}":
        food_options = chicken_options["food_menu"]
        food_descriptions = chicken_options["food_descriptions"]
        food_emoji = chicken_menu_emoji
    else:
        food_options = sushi_options["food_menu"]
        food_descriptions = sushi_options["food_descriptions"]
        food_emoji = sushi_menu_emoji

    menu_options_questions = [
    inquirer.List('food',
                    message=f"What from the {menu_response} would you like to find out more about?",
                    choices=food_options,
                    ),
    ]
    menu_options_response = inquirer.prompt(menu_options_questions)

    view_food_description(menu_options_response["food"], food_descriptions, food_emoji)


def view_food_description(menu_options_response, food_descriptions, food_emoji):

    print(f"{food_emoji} {menu_options_response} {food_emoji} ")
    print(food_descriptions[menu_options_response])

if __name__ == "__main__":
    main()
