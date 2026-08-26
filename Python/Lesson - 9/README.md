# 🐍 Python Mastery — Lesson 9

## Sets & Set Operations

---

## 🎯 Lesson Goal

Lesson 9 introduced **Sets** as a foundational Python collection.

The goal was not simply to learn Set syntax, but to understand:

> **Unique values + membership**

and to learn when a Set is the appropriate tool for organizing information.

---

## 🧠 Core Mental Model

Different collections solve different organization problems:

| Data Structure | Main Mental Model |
|---|---|
| **List** | Ordered collection of values |
| **Tuple** | Ordered collection whose elements cannot be reassigned |
| **Set** | Unique values where membership matters |
| **Dictionary** | Key → associated value |

The important question is:

> **How does the program need to organize and access the information?**

---

# 📚 Concepts Learned

## 1. Why Sets Exist

Sets are useful when the program cares about **uniqueness** rather than keeping duplicate values.

Example:

```python
numbers = {10, 20, 10, 30, 20, 10}
```

The resulting Set contains each distinct value only once.

Mental model:

> **Set = collection of unique elements.**

---

## 2. Creating Sets

A Set can be created with curly braces:

```python
numbers = {1, 2, 3}
```

An important Python distinction:

```python
{}       # empty dictionary
set()    # empty set
```

---

## 3. Duplicate Values

If duplicate values are placed into a Set, the Set keeps only one occurrence of each distinct value.

```python
numbers = {10, 20, 10, 30, 20, 10}

print(numbers)
```

---

## 4. Set Membership

Sets are useful for checking whether an element exists.

```python
students = {"Rudra", "Aarav", "Kabir"}

print("Rudra" in students)
print("Virat" in students)
```

Mental model:

> **Set membership = Does this element exist?**

---

## 5. Set Indexing

Sets are not accessed through numeric indexes like Lists.

```python
numbers = {10, 20, 30}

# This raises TypeError:
# print(numbers[0])
```

Important distinction:

> **List → positional access**

> **Set → membership and unique elements**

---

## 6. Iterating Through a Set

Sets can still be iterated over:

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

The program should not rely on a meaningful positional order when working with a Set.

---

# ➕ Modifying Sets

## 7. Adding Elements with `add()`

```python
students = {"Rudra", "Aarav"}

students.add("Kabir")

print(students)
```

`add()` adds an element if it is not already present.

---

## 8. Adding an Existing Element

```python
students = {"Rudra", "Aarav"}

students.add("Rudra")

print(students)
```

Because `"Rudra"` is already present, the Set's state does not change.

Mental model:

> **Set uniqueness means adding an existing element does not create a duplicate.**

---

## 9. Removing Elements with `remove()`

```python
students = {"Rudra", "Aarav", "Kabir"}

students.remove("Aarav")

print(students)
```

If the element is absent, `remove()` raises an error.

```python
# students.remove("Virat")
```

---

## 10. Removing Elements with `discard()`

```python
students = {"Rudra", "Aarav", "Kabir"}

students.discard("Virat")

print(students)
```

If the element exists, it is removed.

If it does not exist, the Set remains unchanged and no error is raised.

### Important distinction

| Operation | Element Exists | Element Absent |
|---|---|---|
| `add()` | No state change | Adds element |
| `remove()` | Removes element | Error |
| `discard()` | Removes element | No state change |

---

# 🔗 Set Operations

## 11. Union

### Concept

> **Everything from both Sets.**

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

Result:

```text
{1, 2, 3, 4, 5}
```

Method form:

```python
A.union(B)
```

Mental model:

> **Union = everything in A or B.**

---

## 12. Intersection

### Concept

> **Elements common to both Sets.**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)
```

Result:

```text
{3, 4}
```

Method form:

```python
A.intersection(B)
```

Mental model:

> **Intersection = elements in both A and B.**

---

## 13. Difference

### Concept

> **Elements in A but not in B.**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
```

Result:

```text
{1, 2}
```

Method form:

```python
A.difference(B)
```

### Direction matters

```python
A - B
```

is not the same as:

```python
B - A
```

---

## 14. Symmetric Difference

### Concept

> **Elements in either Set, but not in both.**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A ^ B)
```

Result:

```text
{1, 2, 5, 6}
```

Method form:

```python
A.symmetric_difference(B)
```

---

## 🧠 Four Set Operations — Quick Reference

| Operation | Meaning | Python |
|---|---|---|
| **Union** | Everything from both | `A \| B` |
| **Intersection** | Common to both | `A & B` |
| **Difference** | In A, not B | `A - B` |
| **Symmetric Difference** | In either, not both | `A ^ B` |

---

# 🔄 Sets + Previous Collections

## 15. List → Set

A List can be converted to a Set to remove duplicate values:

```python
students = ["Rudra", "Aarav", "Rudra", "Kabir", "Aarav"]

unique_students = set(students)

print(unique_students)
```

---

## 16. List → Set → List

If the final result needs to be a List:

```python
students = ["Rudra", "Aarav", "Rudra", "Kabir", "Aarav", "Virat"]

unique_students = list(set(students))

print(unique_students)
```

Important:

> The intermediate Set removes duplicates, but the resulting List should not be relied on for preserving the original order.

---

## 17. Count Unique Values

```python
students = ["Rudra", "Aarav", "Kabir", "Rudra", "Virat", "Kabir"]

unique_students = set(students)

count = len(unique_students)

print(count)
```

Mental model:

> **Need the number of unique values → Set + `len()`**

---

# 🔗 Sets + Lists + Conditions + Loops

## 18. Find Common Students

```python
morning_batch = ["Rudra", "Aarav", "Kabir", "Virat"]
evening_batch = ["Kabir", "Virat", "Messi", "Neymar"]

morning = set(morning_batch)
evening = set(evening_batch)

common_students = morning & evening

print(common_students)
```

The requirement:

> **Find students present in both batches.**

The chosen operation:

> **Intersection**

---

# 🧪 Problem Solving

## 19. Count Students Appearing More Than Once

This was the final unfamiliar challenge.

Requirement:

> Find which students appear more than once.

The solution used a Dictionary to count occurrences:

```python
students = ["Rudra", "Aarav", "Kabir", "Rudra", "Virat"]

students_dict = {}

for student in students:

    if student in students_dict:
        students_dict[student] += 1
    else:
        students_dict[student] = 1

for key, value in students_dict.items():

    if value > 1:
        print(key)
```

Output:

```text
Rudra
```

This demonstrated that a Set is not automatically the correct solution for every duplicate-related problem.

### Why Dictionary?

The requirement was to know:

> **How many times did each student appear?**

A Dictionary can represent:

```text
student → count
```

For example:

```text
Rudra → 2
Aarav → 1
Kabir → 1
Virat → 1
```

Then the program can select values whose count is greater than `1`.

---

# 🧠 Data-Structure Selection

One of the major goals of Lesson 9 was learning to choose a collection based on the problem.

### List

Choose a List when the program needs an **ordered collection where position matters**.

```python
numbers = [1, 2, 3, 4]
```

### Tuple

Choose a Tuple when the program needs an **ordered collection whose elements should not be reassigned**.

```python
numbers = (1, 2, 3, 4)
```

### Set

Choose a Set when the program needs **unique values and membership**, rather than positional access.

```python
numbers = {1, 2, 3, 4}
```

### Dictionary

Choose a Dictionary when the program needs **meaningful keys associated with values**.

```python
numbers = {
    "a": 1,
    "b": 2
}
```
