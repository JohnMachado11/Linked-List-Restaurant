import inquirer


def start():
    print("Starting")


    questions = [
    inquirer.List('players',
                    message=f"What shall you eat today?",
                    choices=["Chicken", "Soup"],
                    ),
    ]
    response = inquirer.prompt(questions)


if __name__ == "__main__":
    start()
