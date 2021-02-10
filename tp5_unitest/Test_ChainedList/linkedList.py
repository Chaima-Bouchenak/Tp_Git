# coding: utf-8
class Node:
    """ Node of a list """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    """ Linked list """
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def get (self, index):
        """
        Test if node base is emty , raise an exception
        :param node:
        :return:
        """
        if self.head is None:
            raise Exception ("empty node") #exception a la place de ValuError
        else:
            return self.inieme_node_recurs(index, self.head)


    def inieme_node_recurs(self,index,node):
        #print(index, node)
        if node is None:
            return node
        elif index == 0:
            return node
            #raise Exception ("Index over flow")
        else:
            #print("here")
            return self.inieme_node_recurs(index-1, node.next)

    def entire_llist(self):
        string = ""
        for node in self:
            string += str(node)
        return string

    def add_after(self, data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == data:
                new_node.next = node.next
            node.next = new_node
            return

        raise Exception("Node with data '{}' not found".format(data))

    def add_before(self, data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '{}' not found".format(data))

    def remove_node(self, data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '{}' not found".format(data))

    def add_first(self, node_to_add):
        node_to_add.next = self.head
        self.head = node_to_add
    
    def add_last(self, node_to_add):
        if self.head is None:
            self.head = node_to_add
            return

        node = self.head
        # while node.next is not None:*
        while node.next is not None:
            node = node.next
        node.next = node_to_add

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #return "a"
        return "{}".format(nodes)

    def __iter__(self):
        """
        parcourir la lliste avec une boucle
        :return:
        """
        node = self.head
        while node is not None:
            yield node #renvoyer le node et coninue la boucle
            node = node.next
