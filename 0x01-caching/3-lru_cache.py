#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that
    inherits from BaseCaching
    """
    def __init__(self):
        """
        method initialized
        """
        super().__init__()
        self.memory_dic = {}
        self.counter = 0

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.memory_dic[key] = self.counter
            self.counter += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key_min = min(self.memory_dic, key=self.memory_dic.get)
            del self.cache_data[key_min]
            del self.memory_dic[key_min]
            print('DISCARD: {}'.format(key_min))

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.memory_dic[key] = self.counter
        self.counter += 1

        return self.cache_data[key]
