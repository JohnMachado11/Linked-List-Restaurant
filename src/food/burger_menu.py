from data_structure.linked_list import LinkedList
from utils.emojis import burger_emoji
from food.food import Food


burger_menu_emoji = ""

burger_menu = LinkedList()

classic_cheeseburger = Food("Classic Cheeseburger", "Beef patty with cheese and toppings.", burger_emoji)
bacon_burger = Food("Bacon Burger", "Beef patty with bacon and toppings.", burger_emoji)
veggie_burger = Food("Veggie Burger", "Plant-based patty with toppings.", burger_emoji)
mushroom_swiss_burger = Food("Mushroom Swiss Burger", "Beef patty with mushrooms and cheese.", burger_emoji)
bbq_burger = Food("BBQ Burger", "Beef patty with BBQ sauce and toppings.", burger_emoji)
turkey_burger = Food("Turkey Burger", "Turkey patty with toppings.", burger_emoji)
lamb_burger = Food("Lamb Burger", "Lamb patty with toppings.", burger_emoji)
salmon_burger = Food("Salmon Burger", "Salmon patty with toppings.", burger_emoji)
portobello_burger = Food("Portobello Burger", "Grilled portobello mushroom with toppings.", burger_emoji)
black_bean_burger = Food("Black Bean Burger", "Black bean patty with toppings.", burger_emoji)

burger_menu.insert_beginning(classic_cheeseburger)
burger_menu.insert_end(bacon_burger)
burger_menu.insert_end(veggie_burger)
burger_menu.insert_end(mushroom_swiss_burger)
burger_menu.insert_end(bbq_burger)
burger_menu.insert_end(turkey_burger)
burger_menu.insert_end(lamb_burger)
burger_menu.insert_end(salmon_burger)
burger_menu.insert_end(portobello_burger)
burger_menu.insert_end(black_bean_burger)

burger_menu_emoji = burger_menu.show_food_emoji()
