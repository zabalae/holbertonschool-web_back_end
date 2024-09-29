#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that uses the MRU algorithm to
        manage its cache.
    """

    def __init__(self):
        """ Initialize the class, call the parent class __init__ method """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                if self.mru_key:
                    del self.cache_data[self.mru_key]
                    print(f"DISCARD: {self.mru_key}")

            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as the most recently used
        self.mru_key = key
        return self.cache_data.get(key)
