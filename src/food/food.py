
class Food:
    def __init__(self, food_name, food_description, food_emoji):
        self.food_name = food_name
        self.food_description = food_description
        self.food_emoji = food_emoji


    def get_food_name(self):
        return self.food_name


    def get_food_description(self):
        return self.food_description


    def get_food_emoji(self):
        return self.food_emoji
