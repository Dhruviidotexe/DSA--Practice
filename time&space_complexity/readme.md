# Time & Space Complexity

Time and space complexity measure how efficiently an algorithm uses **time** and **memory** as input size `n` grows.

## Time Complexity

| Complexity   | Example              |
| ------------ | -------------------- |
| `O(1)`       | Array access         |
| `O(log n)`   | Binary Search        |
| `O(n)`       | Single loop          |
| `O(n log n)` | Merge Sort           |
| `O(n²)`      | Nested loops         |
| `O(2ⁿ)`      | Recursive algorithms |

## Space Complexity

Measures the **extra memory** used by an algorithm.

```python
# O(n) space
arr = [i for i in range(n)]
```

### Quick Rules

* Drop constants → `O(2n)` → `O(n)`
* Keep the highest term → `O(n² + n)` → `O(n²)`
* Nested loops → usually multiply
* Sequential operations → usually add
