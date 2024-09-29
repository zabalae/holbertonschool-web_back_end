#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that uses the LRU algorithm to
        manage its cache.
    """

    def __init__(self):
        """ Initialize the class, call the parent class __init__ method """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            # Move the key to the end of the list to mark it as recently used
            self.keys_order.remove(key)
            self.keys_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item
                lru_key = self.keys_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new key-value pair
            self.cache_data[key] = item
            self.keys_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as recently used by moving it to the end
        self.keys_order.remove(key)
        self.keys_order.append(key)
        return self.cache_data.get(key)
