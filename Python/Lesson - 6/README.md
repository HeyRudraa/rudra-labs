# Python Mastery — Module 1 — Lesson 6

## What I Learned

### 1. Lists

A list is a collection that can store multiple values together.

```python
marks = [72, 85, 91]
```

Important mental model:

> A collection organizes multiple values so they can be processed together.

---

### 2. List Iteration

A `for` loop can process each value in a list one at a time.

```python
marks = [72, 85, 91]

for mark in marks:
    print(mark)
```

Mental model:

> Collection → next value → loop variable → execute → repeat

---

### 3. Loop Variable vs List

Changing the loop variable does not automatically change the original list.

```python
marks = [72, 85, 91]

for mark in marks:
    mark = mark + 5

print(marks)
```

The list remains unchanged.

Important mental model:

> Changing the loop variable is different from changing an element inside the list.

---

### 4. Modifying List Elements

A list element can be changed using its index.

```python
marks = [72, 85, 91]

for i in range(len(marks)):
    marks[i] = marks[i] + 5

print(marks)
```

Using `marks[i] = ...` writes the new value back into the list at that position.

---

### 5. List Indexing

List indexes start at `0`.

```python
marks = [72, 85, 91, 68]

print(marks[1])
print(marks[3])
print(marks[-1])
```

Negative indexing accesses elements from the end.

```text
Index:     0    1    2    3
Value:    72   85   91   68

Negative: -4   -3   -2   -1
```

---

### 6. Index Modification

An existing element can be replaced using its index.

```python
numbers = [10, 20, 30, 40, 50]

numbers[1] = 99
numbers[-1] = 5
numbers[2] = numbers[0] + numbers[1]

print(numbers)
```

Important distinction:

> Index assignment replaces an existing element.

---

### 7. `append()`

`append()` adds an element to the end of a list.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

`append()` modifies the list but returns `None`.

```python
numbers = [10, 20, 30]

result = numbers.append(40)

print(numbers)
print(result)
```

Important mental model:

> `append()` changes the list but does not return the modified list.

---

### 8. `insert()`

`insert(index, value)` adds a new element at a specific position.

```python
numbers = [10, 20, 30]

numbers.insert(1, 99)

print(numbers)
```

The existing elements shift to the right.

Important distinction:

> `insert()` adds an element.

> Index assignment replaces an element.

---

### 9. `remove()`

`remove(value)` removes the first occurrence of a value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

`remove()` works with a value, not an index.

If the value is found, the first matching element is removed.

If the value is not found, Python raises a `ValueError`.

`remove()` returns `None` when the removal succeeds.

---

### 10. `pop()`

`pop(index)` removes the element at a specific index and returns the removed value.

```python
numbers = [10, 20, 30, 40]

x = numbers.pop(1)

print(numbers)
print(x)
```

`pop()` without an index removes and returns the last element.

```python
numbers = [10, 20, 30]

x = numbers.pop()

print(numbers)
print(x)
```

Important distinction:

> `remove(value)` → remove by value.

> `pop(index)` → remove by index and return the removed value.

> `pop()` → remove and return the last element.

---

### 11. `len()`

`len()` tells us how many elements are currently in a collection.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Important distinction:

> Length is the number of elements, while the last index is one less than the length.

For example:

```text
Index:   0   1   2   3
Value:  10  20  30  40

Length = 4
Last index = 3
```

`len()` counts elements such as `""` and `None` because they are still elements in the list.

---

### 12. Membership with `in`

`in` checks whether a value exists in a collection.

```python
names = ["Rudra", "Messi", "Argentina"]

print("Messi" in names)
print("Brazil" in names)
```

The result is a Boolean:

```text
True
False
```

Mental model:

> `value in collection` → Does this value exist in the collection?

---

### 13. Membership with `not in`

`not in` checks whether a value does not exist in a collection.

```python
names = ["Rudra", "Messi", "Argentina"]

print("Ronaldo" not in names)
print("Messi" not in names)
```

The result is also a Boolean.

---

### 14. Membership + Conditions

Membership checks can be combined with `if/else`.

```python
marks = [45, 72, 88, 39, 91]

if 50 in marks:
    print("Found")
else:
    print("Not Found")
```

This combines:

> Collection + membership + conditional logic

---

### 15. Basic Slicing

Slicing allows multiple elements to be accessed at once.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[2:5])
```

Important mental model:

> `start` is included and `stop` is excluded.

This is the same inclusive-start / exclusive-stop idea used with `range()`.

---

### 16. Slicing Beyond Available Indexes

Slicing behaves differently from direct index access.

A direct index outside the valid range raises an `IndexError`.

A slice that extends beyond the available list does not raise an error.

```python
numbers = [10, 20, 30]

print(numbers[1:10])
```

The slice returns the elements that are available.

---

## List Mental Models

> Collection → values organized together

> Index → position used to access an element

> `append()` → add to the end

> `insert()` → add at a position

> Index assignment → replace an element

> `remove()` → remove by value

> `pop()` → remove by index or last element and return it

> `len()` → number of elements

> `in` → membership test

> Slicing → access a range of elements

---

## Practical Work

During this lesson, I practiced combining lists with:

- `for` loops
- `range()`
- `len()`
- `if/else`
- membership checks
- indexing
- negative indexing
- modification
- `append()`
- `insert()`
- `remove()`
- `pop()`
- slicing
- state tracing
- cumulative challenges

The main progression was:

> Understand → Predict → Modify → Build → Debug → Apply
