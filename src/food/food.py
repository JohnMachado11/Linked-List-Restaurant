
class Food:
    def __init__(self, name, description, emoji):
        self.name = name
        self.description = description
        self.emoji = emoji


    def get_food_name(self):
        return self.name


    def get_food_description(self):
        return self.description


    def get_food_emoji(self):
        return self.emoji
