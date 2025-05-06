import unittest
from LruCache import LRUCache  # Make sure your main file is named lru_cache.py

class TestLRUCache(unittest.TestCase):

    def test_basic_get_put(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)  # recently used now
        lru.put(3, 3)  # evicts key 2
        self.assertEqual(lru.get(2), -1)
        self.assertEqual(lru.get(3), 3)

    def test_overwrite_existing_key(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(1, 10)  # update value
        self.assertEqual(lru.get(1), 10)

    def test_eviction_order(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        lru.get(1)      # 1 is now recently used
        lru.put(3, 3)   # evicts key 2
        self.assertEqual(lru.get(2), -1)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(3), 3)

    def test_empty_cache(self):
        lru = LRUCache(2)
        self.assertEqual(lru.get(100), -1)  # non-existent key

if __name__ == '__main__':
    unittest.main()
