from data_structure.linked_list import LinkedList
from utils.emojis import sushi_emoji
from food.food import Food


sushi_menu_emoji = ""

sushi_menu = LinkedList()

california_roll = Food("California Roll", "Sushi roll with avocado and crab.", sushi_emoji)
spicy_tuna_roll = Food("Spicy Tuna Roll", "Sushi roll with tuna and spicy sauce.", sushi_emoji)
salmon_nigiri = Food("Salmon Nigiri", "Sliced salmon on rice.", sushi_emoji)
tofu_teriyaki = Food("Tofu Teriyaki", "Grilled tofu with teriyaki sauce.", sushi_emoji)
shrimp_tempura_roll = Food("Shrimp Tempura Roll", "Sushi roll with fried shrimp.", sushi_emoji)
dragon_roll = Food("Dragon Roll", "Sushi roll with eel and avocado.", sushi_emoji)
vegetable_roll = Food("Vegetable Roll", "Sushi roll with various vegetables.", sushi_emoji)
philly_roll = Food("Philly Roll", "Sushi roll with cream cheese and salmon.", sushi_emoji)
yellowtail_scallion_roll = Food("Yellowtail Scallion Roll", "Sushi roll with yellowtail and scallions.", sushi_emoji)
spider_roll = Food("Spider Roll", "Sushi roll with fried soft-shell crab.", sushi_emoji)

sushi_menu.insert_beginning(california_roll)
sushi_menu.insert_end(spicy_tuna_roll)
sushi_menu.insert_end(salmon_nigiri)
sushi_menu.insert_end(tofu_teriyaki)
sushi_menu.insert_end(shrimp_tempura_roll)
sushi_menu.insert_end(dragon_roll)
sushi_menu.insert_end(vegetable_roll)
sushi_menu.insert_end(philly_roll)
sushi_menu.insert_end(yellowtail_scallion_roll)
sushi_menu.insert_end(spider_roll)

sushi_menu_emoji = sushi_menu.show_food_emoji()
