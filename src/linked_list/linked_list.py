from node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None


    def get_head_node(self):
        return self.head_node


    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head_node == None:
            self.head_node = new_node
        else:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node


    def insert_end(self, data):
        new_node = Node(data)
        if self.head_node == None:
            self.head_node = new_node
        else:
            current_node = self.get_head_node()
            while current_node.get_next_node() != None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)
            print(f"New node added {current_node.get_next_node().get_node_data()}")


    def display_list(self):
        current_node = self.get_head_node()
        contents = ""
        while current_node:
            contents += "{} -> ".format(current_node.get_node_data().get_food_name())
            current_node = current_node.get_next_node()
        contents += "None"
        return contents


class Food:
    def __init__(self, food_name):
        self.food_name = food_name

    
    def get_food_name(self):
        return self.food_name


chicken_options = LinkedList()
chicken_teriyaki = Food("Chicken Teriyaki")
chicken_soup = Food("Chicken Soup")
chicken_options.insert_beginning(chicken_teriyaki)
chicken_options.insert_end(chicken_soup)


print(chicken_options.get_head_node().get_node_data().get_food_name())

print(chicken_options.display_list())

# print(chicken_teriyaki.get_food_name())
# pasta_options = Food("Chicken Teriyaki")
# chicken_menu = Food("Chicken Teriyaki")


# ll.insert_beginning(2) # temp
# ll.insert_beginning(55) # temp
# ll.insert_beginning(23) # temp

# print(ll.get_head_node().get_node_data())
