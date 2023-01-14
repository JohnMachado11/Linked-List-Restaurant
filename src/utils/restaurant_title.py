from utils.emojis import burger_emoji, chicken_emoji, sushi_emoji
from time import sleep
import pyfiglet


def title():
    linked_list_restaurant = pyfiglet.figlet_format("Linked - List Restaurant", font="slant")

    food_emojis = (burger_emoji + chicken_emoji + sushi_emoji + " ") * 6

    count = 0
    for _ in range(2):
        count += 1
        for i in range(len(food_emojis)):
            print(food_emojis[i], sep=' ', end=' ', flush=True); sleep(0.04)
        if count == 2:
            break
        else:
            print(), print(), print(linked_list_restaurant)
    print(), sleep(1), print()
