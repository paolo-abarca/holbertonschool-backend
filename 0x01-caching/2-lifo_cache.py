#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that
    inherits from BaseCaching
    """
    def __init__(self):
        """
        method initialized
        """
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.key_delete]
            print('DISCARD: {}'.format(self.key_delete))

        if key in self.cache_data:
            self.key_delete = key

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
