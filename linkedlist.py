from node import*

class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList.
        """
        self.head = None

    def append(self, value):
        """
        Append a new element to the end of the LinkedList.

        Args:
            value: The value of the element to append.
        """
        node = Node(value)  # creating new node with value

        # if the LinkedList is empty
        if self.head is None:
            self.head = node
        else:  # LinkedList is not empty
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __getitem__(self, index):
        """
        Get the value of the element at a specific index in the LinkedList.

        Args:
            index: The index of the element.

        Returns:
            The value of the element at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1
        raise IndexError("Index out of range")

    def __len__(self):
        """
        Get the number of elements in the LinkedList.

        Returns:
            The number of elements in the LinkedList.
        """
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        return len

    def __str__(self):
        """
        Convert the LinkedList to a string.

        Returns:
            A string representation of the LinkedList.
        """
        str = ""
        current = self.head
        while current:
            str += current.val + "-->"
            current = current.next
        return str
