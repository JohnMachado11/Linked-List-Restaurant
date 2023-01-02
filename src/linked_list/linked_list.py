from linked_list.node import Node


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
            # print(f"New node added {current_node.get_next_node().get_node_data()}")


    def show_menu(self):
        current_node = self.get_head_node()
        print(current_node)
        menu = []
        while current_node:
            menu.append(current_node.get_node_data().get_food_name())
            current_node = current_node.get_next_node()
        return menu


    # For Debugging
    def display_list(self):
        current_node = self.get_head_node()
        contents = ""
        while current_node:
            contents += "{} -> ".format(current_node.get_node_data().get_food_name())
            current_node = current_node.get_next_node()
        contents += "None"
        return contents
