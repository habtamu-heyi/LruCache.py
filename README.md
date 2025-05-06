# 🔁 LRU Cache in Python

This project implements a high-performance **Least Recently Used (LRU) Cache** using a combination of **Doubly Linked List** and **Hash Map** in Python. It ensures constant time complexity — **O(1)** — for both `get` and `put` operations.

---

## 🚀 Features

- ✅ O(1) time complexity for both access and update
- ✅ Automatic eviction of least recently used items when capacity is exceeded
- ✅ Clean and well-structured object-oriented design
- ✅ No external libraries required

---

## 📚 How It Works

- A **Hash Map (`dict`)** allows fast lookup of cache items by key.
- A **Doubly Linked List** tracks the order of usage:
  - Most recently used items are at the front.
  - Least recently used items are at the back.
- When the cache exceeds its capacity, the least recently used item is removed (from the end of the list).

---

## 🧠 Data Structures Used

| Component        | Purpose                                |
|------------------|----------------------------------------|
| `dict` (hash map) | O(1) key-to-node lookup                |
| Doubly Linked List | O(1) insertions & deletions from ends |

---

## 🛠️ Usage Example

```python
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # Output: 1
lru.put(3, 3)      # Evicts key 2
print(lru.get(2))  # Output: -1 (not found)
print(lru.get(3))  # Output: 3
