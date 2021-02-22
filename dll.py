class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.position = 1                                       # Initial position at trailer since
        self.size = 0                                           # trailer index increments with new data

    def get_current_node(self, pos):
        """Navigate to correct node"""
        node = self.header
        for _ in range(self.position):
            node = node.next
        return node

    def relink(self, current, predecessor, successor):
        """Link new node"""

        current.next = successor                            # Links from new node
        if current != predecessor:
            current.prev = predecessor                          # -------------------

        try:                                                    # Links to new node
            predecessor.next = current
        except AttributeError:
            self.header.next = current
        try:
            successor.prev = current
        except AttributeError:
            self.trailer.prev = current                         # -------------------

    def insert(self, data):
        successor = self.get_current_node(self.position)
        predecessor = successor.prev
        newest = Node(data, successor.prev, successor)
        successor.prev = newest
        self.relink(newest, predecessor, successor)
        self.size += 1


    def remove(self):
        if self.size > 0:
            # removed = self.header.next
            # successor = removed.next
            # successor.prev = self.header
            # self.header.next = successor
            # self.size -= 1
            # if self.position >= self.size:
            #     self.position -= 1
            removed = self.get_current_node(self.position)
            successor = removed.next
            predecessor = removed.prev
            self.relink(predecessor, predecessor, successor)

            data = removed.data                                 # Record data deletion
            removed.data = removed.prev = removed.next = None   # Deprecate node
            return data                                         # Return deleted data
        else:
            pass

    def get_value(self):
        # node = self.header.next
        # for _ in range(self.position-1):
        #     node = node.next
        node = self.get_current_node(self.position)
        return node.data

    def move_to_next(self):
        if self.position < self.size:
            self.position += 1
        else:
            pass

    def move_to_prev(self):
        if self.position > 1:
            self.position -= 1

    def move_to_pos(self, pos):
        if pos > 0 and pos < self.size:
            self.position = pos+1

    def clear(self):
        for _ in range(self.size):
            self.remove()

    def get_first_node(self):
        return self.header.next

    def get_last_node(self):
        return self.trailer.prev

    def partition(self, low, high):
        pass

    def sort(self):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        ret_list = [0]*self.size
        temp_var = self.header.next
        for _ in range(self.size):
            ret_list[_] = temp_var.data
            temp_var = temp_var.next
        return ' '.join([str(value) for value in ret_list])

if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("E")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # print(dll.position)
    dll.insert("1")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))