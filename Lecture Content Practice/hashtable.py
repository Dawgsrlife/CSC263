from typing import Any


class HashTable:
    """
    A simple hash table implementation using separate chaining.

    === Public Attributes ===
    _items: A list of lists, where each list represents a bucket for chaining.
    _capacity: The number of buckets in the hash table.
    _size: The number of key-value pairs stored in the hash table.

    === Representation Invariants ===
    - 0 <= self._size <= self._capacity
    """
    _items: list[list[Any]]
    _capacity: int
    _size: int

    def __init__(self, capacity: int = 10) -> None:
        """
        Initialize a hash table with the given capacity.
        """
        self._capacity = capacity
        self._size = 0
        self._items = [[] for _ in range(capacity)]

    def _hash(self, key) -> int:
        """
        Compute the hash index for the given key.
        """
        return hash(key) % self._capacity

    def search(self, k):
        """
        Retrieve the value associated with the given key.
        Raise KeyError if the key does not exist.
        """
        index = self._hash(k)
        bucket = self._items[index]

        for key, value in bucket:
            if key == k:
                return value

        raise KeyError(f'Key {k} not found')

    def insert(self, x) -> None:
        """
        Insert a new item into the hash table.
        If the key already exists, update its value.
        """
        key, value = x
        index = self._hash(key)
        bucket = self._items[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        bucket.append((key, value))  # Insert new key-value pair
        self._size += 1

    def delete(self, x) -> None:
        """
        Remove the item with the given key from the hash table.
        Raise KeyError if the key does not exist.
        """
        key = x
        index = self._hash(key)
        bucket = self._items[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return

        raise KeyError(f'Key {key} not found')
