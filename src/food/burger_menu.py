from data_structure.linked_list import LinkedList
from food.food import Food


burger_menu = LinkedList()

classic_cheeseburger = Food("Classic Cheeseburger", "Beef patty with cheese and toppings.")
bacon_burger = Food("Bacon Burger", "Beef patty with bacon and toppings.")
veggie_burger = Food("Veggie Burger", "Plant-based patty with toppings.")
mushroom_swiss_burger = Food("Mushroom Swiss Burger", "Beef patty with mushrooms and cheese.")
bbq_burger = Food("BBQ Burger", "Beef patty with BBQ sauce and toppings.")
turkey_burger = Food("Turkey Burger", "Turkey patty with toppings.")
lamb_burger = Food("Lamb Burger", "Lamb patty with toppings.")
salmon_burger = Food("Salmon Burger", "Salmon patty with toppings.")
portobello_burger = Food("Portobello Burger", "Grilled portobello mushroom with toppings.")
black_bean_burger = Food("Black Bean Burger", "Black bean patty with toppings.")

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