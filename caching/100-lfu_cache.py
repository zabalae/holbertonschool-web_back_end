#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that uses the LFU algorithm to
        manage its cache. If multiple items have the same frequency,
        the LRU (Least Recently Used) algorithm is applied.
    """

    def __init__(self):
        """ Initialize the class, call the parent class __init__ method """
        super().__init__()
        self.keys_order = []
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            # Increment the frequency count
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

                # If there are multiple least frequently used, apply LRU
                if len(lfu_keys) > 1:
                    lfu_key = next(k for k in self.keys_order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                # Discard the least frequently used item
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.keys_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.keys_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency count
        self.frequency[key] += 1

        # Move the key to the end of the order to mark it as recently used
        self.keys_order.remove(key)
        self.keys_order.append(key)

        return self.cache_data.get(key)
