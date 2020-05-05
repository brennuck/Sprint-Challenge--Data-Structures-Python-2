from doubly_linked_list import DoublyLinkedList

# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: # If the storage is less than the capacity
            self.storage.add_to_tail(item) # Add given item to the back of the buffer
            self.current = self.storage.head # Current node is the top node
        elif self.storage.length == self.capacity: # if the storage is equal to the capacity
            to_delete = self.storage.head # gonna delete the head
            self.storage.remove_from_head() # Remove the head node from the buffer
            self.storage.add_to_tail(item) # Add the new given item to the tail
            if to_delete == self.current: # if the to_deleted node is the current node
                self.current = self.storage.tail # new current is the tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        initial_node = self.current # initial node is the current node
        list_buffer_contents.append(initial_node.value) # add the initial node to the contents

        if initial_node.next is not None: # if the next node after the head is not none
            next_node = initial_node.next # then next node is the next node
        else: # if there isn't another node
            next_node = self.storage.head # then the next node is the top node

        while next_node != initial_node: # while the next node is not the initail node
            list_buffer_contents.append(next_node.value) # add the the next nodes values
            if next_node.next is not None: # if the next node is not none
                next_node = next_node.next # move on to the next node
            else: # if there isn't another node
                next_node = self.storage.head # make the top node the next node

        return list_buffer_contents # return the contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
