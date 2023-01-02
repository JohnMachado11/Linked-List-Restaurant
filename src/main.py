from food.chicken_menu import chicken_menu
import inquirer


# -------------------  Important Variables -------------------
menu_options = ["Chicken Menu", "Burger Menu", "Sushi Menu"]
chicken_options = chicken_menu.show_menu()
# burger_options = burger_menu.show_menu() # Need to implement
# sushi_options = sushi_menu.show_menu() # Need to implement
# ------------------------------------------------------------


# Create single function to show user all food options from menu they select
# Create single function to show user description of food they select from food options

def start():
    print("Starting")

    questions = [
    inquirer.List('menu',
                    message=f"What menu would you like to see?",
                    choices=menu_options,
                    ),
    ]
    response = inquirer.prompt(questions)

    # Logic needs to be added here to select correct food option based off user response

    questions = [
    inquirer.List('menu_options',
                    message=f"What from the Chicken Menu would you like to find out more about?",
                    choices=chicken_options,
                    ),
    ]
    response = inquirer.prompt(questions)


if __name__ == "__main__":
    start()
