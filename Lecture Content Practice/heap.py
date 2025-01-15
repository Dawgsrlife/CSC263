#######################################
# Author: AlexanderTheMango
# Course: CSC263 at UTM
# Date: January 15th, 2025
# Description: MaxHeap Implementation
#######################################

class MaxHeap:
    """
    A class to represent a binary max-heap.

    Methods:
        - __init__: Initializes an empty heap.
        - parent(index: int) -> int: Returns the parent index of a given index.
        - left_child(index: int) -> int: Returns the left child index of a given index.
        - right_child(index: int) -> int: Returns the right child index of a given index.
        - insert(key: int) -> None: Inserts a new key into the heap.
        - extract_max() -> int: Removes and returns the maximum element in the heap.
        - increase_priority(index: int, new_value: int) -> None: Increases the value at a given index.
        - max() -> int: Returns the maximum element without removing it.
    """

    def __init__(self):
        """
        Initializes an empty max-heap.
        """
        self.heap = []  # Represent the heap as a list

    def parent(self, index: int) -> int:
        """
        Returns the parent index of a given index.
        
        :param index: Index of the current node.
        :return: Index of the parent node.
        """
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        """
        Returns the left child index of a given index.
        
        :param index: Index of the current node.
        :return: Index of the left child.
        """
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        """
        Returns the right child index of a given index.
        
        :param index: Index of the current node.
        :return: Index of the right child.
        """
        return 2 * index + 2

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the heap and restores the heap property by bubbling up.
        
        :param key: The key to insert.
        """
        self.heap.append(key)  # Add the new key to the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property

    def extract_max(self) -> int:
        """
        Removes and returns the maximum element (root) from the heap.
        
        :return: The maximum element in the heap.
        :raises IndexError: If the heap is empty.
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, just pop and return it

        max_value = self.heap[0]  # The root is the maximum value
        self.heap[0] = self.heap.pop()  # Replace root with the last element and remove it
        self._bubble_down(0)  # Restore the heap property by bubbling down
        return max_value

    def increase_priority(self, index: int, new_value: int) -> None:
        """
        Increases the priority of the element at a given index to a new value.
        The heap property is restored by bubbling up.
        
        :param index: Index of the element to increase.
        :param new_value: The new value to assign (must be greater than the current value).
        :raises ValueError: If the new value is less than the current value.
        """
        if new_value < self.heap[index]:
            raise ValueError("New value must be larger than the current value")
        self.heap[index] = new_value  # Update the value
        self._bubble_up(index)  # Restore the heap property

    def max(self) -> int:
        """
        Returns the maximum element without removing it.
        
        :return: The maximum element in the heap.
        :raises IndexError: If the heap is empty.
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]  # The root contains the maximum value

    def _bubble_up(self, index: int) -> None:
        """
        Restores the heap property by bubbling up the element at the given index.
        
        :param index: Index of the element to bubble up.
        """
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap the element with its parent
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)  # Move up to the parent's index

    def _bubble_down(self, index: int) -> None:
        """
        Restores the heap property by bubbling down the element at the given index.
        
        :param index: Index of the element to bubble down.
        """
        size = len(self.heap)
        while True:
            largest = index  # Assume the current index is the largest
            left = self.left_child(index)
            right = self.right_child(index)

            # Check if left child exists and is larger than current largest
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            # Check if right child exists and is larger than current largest
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # If largest is not the current index, swap and continue
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest  # Update index to the largest child's index
            else:
                break  # The heap property is satisfied

    def __str__(self) -> str:
        """
        Returns a string representation of the heap.
        
        :return: A string showing the heap elements.
        """
        return str(self.heap)
