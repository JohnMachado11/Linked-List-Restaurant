from utils.emojis import burger_emoji, chicken_emoji, sushi_emoji
from time import sleep
import pyfiglet


def title():
    
    linked_list_restaurant = pyfiglet.figlet_format("Linked - List Restaurant", font="slant")
    food_emojis = (burger_emoji + chicken_emoji + sushi_emoji + " ") * 6

    print()

    for i in range(2):
        for j in range(len(food_emojis)):
            print(food_emojis[j], sep=' ', end=' ', flush=True) 
            sleep(0.04)
        if i != 1:
            print()
            print()
            print(linked_list_restaurant)

    print() 
    sleep(1) 
    print()
