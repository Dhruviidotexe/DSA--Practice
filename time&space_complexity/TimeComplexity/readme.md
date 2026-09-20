# Time Complexity

## Introduction

**Time Complexity** describes how the running time of an algorithm grows as the input size `n` increases.

It helps us compare algorithms and understand which one is more efficient.

We use **Asymptotic Notation** to represent time complexity.

---

## Types of Analysis

### 1. Best Case

The **minimum time** an algorithm takes for an input.

Example: Searching for an element that is the **first element**.

```python
arr = [10, 20, 30, 40]

# Searching for 10
```

Best Case: `O(1)`

### 2. Average Case

The **expected time** an algorithm takes for a typical input.

Example: Searching for an element that may be somewhere in the middle.

### 3. Worst Case

The **maximum time** an algorithm can take for an input.

Example: Searching for an element that is the **last element** or not present.

Worst Case: `O(n)`

---

# Asymptotic Notations

## Big O — `O`

Describes the **upper bound** of an algorithm's growth.

It is commonly used to describe **worst-case complexity**.

Example:

```python
for i in range(n):
    print(i)
```

Time Complexity: `O(n)`

---

## Omega — `Ω`

Describes the **lower bound** of an algorithm's growth.

It is commonly used to describe the **best-case complexity**.

Example:

For linear search:

* Best Case: `Ω(1)`
* Element found at the first position.

---

## Theta — `Θ`

Describes the **exact/asymptotically tight bound** when the upper and lower bounds are the same.

Example:

```python
for i in range(n):
    print(i)
```

Time Complexity: `Θ(n)`

The loop always runs `n` times.

---

# Common Time Complexities

| Complexity   | Name         | Example                 |
| ------------ | ------------ | ----------------------- |
| `O(1)`       | Constant     | Array access            |
| `O(log n)`   | Logarithmic  | Binary Search           |
| `O(n)`       | Linear       | Single loop             |
| `O(n log n)` | Linearithmic | Merge Sort              |
| `O(n²)`      | Quadratic    | Nested loops            |
| `O(2ⁿ)`      | Exponential  | Recursive Fibonacci     |
| `O(n!)`      | Factorial    | Generating permutations |

---

## Examples

### O(1) — Constant

```python
print(arr[0])
```

Takes the same amount of work regardless of `n`.

---

### O(n) — Linear

```python
for i in range(n):
    print(i)
```

Work increases with `n`.

---

### O(n²) — Quadratic

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Two nested loops → `O(n²)`.

---

### O(log n) — Logarithmic

```python
# Binary Search
```

The search space is divided in half at each step.

---

## Important Rules

* Ignore constants: `O(2n)` → `O(n)`
* Keep the highest-order term: `O(n² + n)` → `O(n²)`
* Sequential loops usually add: `O(n) + O(n)` → `O(n)`
* Nested loops usually multiply: `O(n) × O(n)` → `O(n²)`
* Complexity describes **growth**, not the exact execution time.

## Quick Summary

**Best Case →** minimum operations
**Average Case →** expected operations
**Worst Case →** maximum operations

**Big O →** Upper Bound
**Ω (Omega) →** Lower Bound
**Θ (Theta) →** Tight Bound
