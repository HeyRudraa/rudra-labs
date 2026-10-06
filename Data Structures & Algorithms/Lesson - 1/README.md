# DSA Foundations — Lesson 1

This is my work from **Module 3 — Data Structures & Algorithms, Chapter 1, Lesson 1**.

In this lesson I started building the foundation of DSA by understanding how data structures and algorithms work together and why the choice of data structure or algorithm matters.

## What I Learned

- What data means in programming
- What a data structure is
- What an algorithm is
- Why the required operation affects the data structure we choose
- Why a `set` is useful for membership checking
- Why a `dict` is useful for key → value relationships
- How linear search works
- How binary search works on sorted data
- Why binary search cannot safely eliminate halves when data is not sorted
- Why algorithm efficiency matters as input size grows
- How to think about edge cases

## What I Built

I implemented small Python programs for:

- Checking whether a student exists using a `set`
- Looking up student marks using a `dict`
- Implementing linear search manually
- Handling an empty-list search case
- Implementing binary search on sorted data

## Concepts Covered

### Data Structures

```text
list       → ordered collection
set        → membership and unique values
dict       → key → value relationships
tuple      → fixed collection
```

### Searching

**Linear Search**

Checks elements one by one until the target is found or the collection ends.

**Binary Search**

Works on sorted data and repeatedly reduces the search range by roughly half.

## Example

For linear search:

```text
[4, 8, 2, 9, 1, 7]

Search: 9

4 → no
8 → no
2 → no
9 → found
```

For binary search, the important idea is that sorted order lets us decide which half of the remaining data can be ignored.

## Key Takeaway

The main thing I understood from this lesson is that DSA is not just about memorizing data structures and algorithms.

I should first understand:

```text
What data do I have?
        ↓
What operations do I need?
        ↓
How should I represent the data?
        ↓
Which algorithm makes sense?
        ↓
What edge cases should I consider?
```

This gives me a foundation for solving more difficult DSA problems later.
