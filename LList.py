# Bhavana Samudrala
class node(object):
    """ A version of the Node class with public attributes.
        This makes the use of node objects a bit more convenient for 
        implementing LList class.  
        
        Since there are no setters and getters, we use the attributes directly.
        
        This is safe because the node class is defined in this module.  
        No one else will use this version of the class.
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.data = data  # Any data value to be stored in the node
        self.next = next  # Another node (or None, by default)

    # Note: use the attributes directly; no setters or getters!


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None  # the node chain ends here; initially empty

    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """
        return self._size == 0  # returns true if there is no data in the list

    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size  # returns the size of the list if there is data in the list

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        n = node(val)
        n.next = self._head  # inserting the value at the front of the node chain
        self._head = n
        if self._tail == None:
            self._tail = n
        self._size = self._size+1  # incrementing the list size with 1
        return None

    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """

        n = node(val)
        if self._head is None:
            self._head = n
        if self._tail is not None:
            self._tail.next = n
        self._tail = n

        self._size = self._size+1  # incrementing the list size with 1



    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """
        idx=0
        if self._head is None:
            print("empty")
            return False,None # if the vale does not appear in self
        n = self._head
        while n is not None:
            idx = idx + 1  # incrementing the index value with 1
            if n.data == val:
                print("Item found")
                return True, idx-1  # if the val appears in self
            n = n.next
        print(" not found")
        return False, None # if the vale does not appear in self

    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value 
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if not(self.is_empty()):
            n = self._head
            val = n.data
            n = n.next()
            self._size = self._size-1  # decrementing the list size with 1
            self._head = n
            if self._size == 0:
                self._tail = None
            return True, val
        else:
            return False, None


    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """

        n = self._head
        if self._head == None:
            return False, None  # The pair False, None if self is empty
        if n.next() == None:
            self._head = None
            self._tail = None
            return False, None  # The pair False, None if self is empty
        second_last = n.next()
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        self._size = self._size - 1  # decrementing the list size with 1
        return True, self._head  # The pair True, value if self is not empty


    def retrieve_data(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """
        current = self._head
        count = 0

        while current:
            if count == idx:  # val is stored at index idx
                return True, current.data
            count += 1   # incrementing the count with 1
            current = current.next  # going to the next node
        return False, None

    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        n = self._head
        count = 0
        if idx < self._size and idx >= 0:
            while idx > 0:
                idx = idx-1  # decrementing the index with 1
                n = n.next
            n.data = val
            return True

        return False
