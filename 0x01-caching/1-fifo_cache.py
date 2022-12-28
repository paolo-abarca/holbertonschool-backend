#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that
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
            key_delete = list(self.cache_data)[0]
            del self.cache_data[key_delete]
            print('DISCARD: {}'.format(key_delete))

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
