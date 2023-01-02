
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def get_node_data(self):
        return self.data


    def get_next_node(self):
        return self.next


    def set_next_node(self, new_node):
        self.next = new_node


    def get_object_data(self):
        pass
