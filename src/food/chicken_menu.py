from data_structure.linked_list import LinkedList
from food.food import Food


chicken_menu = LinkedList()

chicken_parmesan = Food("Chicken Parmesan", "Breaded chicken with tomato sauce.")
grilled_chicken_salad = Food("Grilled Chicken Salad", "Greens with grilled chicken slices.")
chicken_alfredo_pasta = Food("Chicken Alfredo Pasta", "Pasta with chicken and creamy sauce.")
bbq_chicken_sandwhich = Food("BBQ Chicken Sandwich", "Sandwich with BBQ sauce and chicken.")
crispy_chicken_strips = Food("Crispy Chicken Strips", "Fried chicken strips with dipping sauce.")
chicken_fajitas = Food("Chicken Fajitas", "Chicken and vegetables in a tortilla.")
roasted_chicken = Food("Roasted Chicken", "Whole roasted chicken with vegetables.")
chicken_noodle_soup = Food("Chicken Noodle Soup", "Chicken and noodles in broth.")
lemon_garlic_chicken = Food("Lemon Garlic Chicken", "Chicken with lemon and garlic flavors.")
honey_mustard_chicken = Food("Honey Mustard Chicken", "Chicken with honey mustard sauce.")

chicken_menu.insert_beginning(chicken_parmesan)
chicken_menu.insert_end(grilled_chicken_salad)
chicken_menu.insert_end(chicken_alfredo_pasta)
chicken_menu.insert_end(bbq_chicken_sandwhich)
chicken_menu.insert_end(crispy_chicken_strips)
chicken_menu.insert_end(chicken_fajitas)
chicken_menu.insert_end(roasted_chicken)
chicken_menu.insert_end(chicken_noodle_soup)
chicken_menu.insert_end(lemon_garlic_chicken)
chicken_menu.insert_end(honey_mustard_chicken)
