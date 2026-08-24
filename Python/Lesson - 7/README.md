# 🐍 Python Mastery — Module 1 — Lesson 7

# What I Learned

## 1. Tuples

A tuple is an ordered collection of values.

```python
numbers = (10, 20, 30)
```

Tuples support:

- storing multiple values
- indexing
- negative indexing
- slicing
- iteration
- searching
- counting

---

## 2. Tuple Creation

A tuple can contain multiple values:

```python
numbers = (10, 20, 30)
```

An empty tuple:

```python
empty = ()
```

A single-element tuple requires a comma:

```python
single = (10,)
```

Important distinction:

```python
(10)   # int
(10,)  # tuple
```

The comma is what makes the single value a tuple.

Tuple parentheses can also be omitted in some cases:

```python
numbers = 10, 20
```

This creates:

```python
(10, 20)
```

---

## 3. Tuple Indexing

Tuples use zero-based indexing.

```python
data = (50, 100, 150, 200)

print(data[0])   # 50
print(data[2])   # 150
print(data[-1])  # 200
```

The same basic indexing model used with lists applies to tuples.

---

## 4. Tuple Slicing

Tuples support slicing.

```python
numbers = (10, 20, 30, 40, 50)

result = numbers[1:4]
```

Result:

```python
(20, 30, 40)
```

Slicing does not modify the original tuple.

The resulting sequence keeps the same sequence type:

```python
[10, 20, 30][1:3]     # list
(10, 20, 30)[1:3]     # tuple
```

---

## 5. Tuple Iteration

Tuples can be iterated using `for`.

```python
numbers = (5, 10, 15, 20)

total = 0

for number in numbers:
    total += number
```

The loop accesses each value without modifying the tuple.

Mental model:

> Collection → one value at a time → process → next value

---

## 6. Tuple Immutability

A tuple's existing elements cannot be reassigned.

This is not allowed:

```python
data = (10, 20, 30)

data[0] = 99
```

It produces an error because it attempts to modify an existing tuple element.

Mental model:

> Tuple element → cannot be reassigned

---

## 7. Immutability vs Reassignment

Immutable does not mean that the variable can never refer to another tuple.

This is allowed:

```python
data = (10, 20, 30)

data = (99, 20, 30)
```

The original tuple is not modified.

The variable is simply reassigned to another tuple.

Tuple concatenation works similarly:

```python
data = (10, 20, 30)

data = data + (40,)
```

A new tuple is created:

```python
(10, 20, 30, 40)
```

and `data` is reassigned to it.

Important distinction:

> Modify existing tuple → not allowed

> Create new tuple and reassign variable → allowed

---

## 8. Tuples Can Contain Mutable Objects

A tuple can contain objects that are themselves mutable.

Example:

```python
data = ([1, 2], 3)

data[0].append(4)
```

Result:

```python
([1, 2, 4], 3)
```

The tuple itself was not structurally changed.

The list stored inside the tuple was modified.

Important mental model:

> Tuple immutability applies to the tuple's own elements and their reassignment. It does not automatically make objects stored inside the tuple immutable.

---

## 9. Tuple Length and Membership

Tuples work with `len()`:

```python
numbers = (10, 20, 30)

len(numbers)
```

Result:

```python
3
```

Membership can be checked using `in`:

```python
20 in numbers
```

Result:

```python
True
```

And:

```python
99 in numbers
```

Result:

```python
False
```

---

## 10. `count()`

The `count()` method tells how many times a value occurs.

```python
numbers = (10, 20, 30, 20, 40)

numbers.count(20)
```

Result:

```python
2
```

Mental model:

> `count(value)` → How many times does this value occur?

---

## 11. `index()`

The `index()` method returns the index of the first occurrence of a value.

```python
numbers = (10, 20, 30, 20, 40)

numbers.index(20)
```

Result:

```python
1
```

Even though `20` occurs again later, `index()` returns the position of the first occurrence.

Mental model:

> `index(value)` → Where is the first occurrence?

---

## 12. `count()` vs `index()`

These methods answer different questions.

```python
numbers.count(20)
```

asks:

> How many?

Result:

```python
2
```

While:

```python
numbers.index(20)
```

asks:

> Where is the first one?

Result:

```python
1
```

---

## 13. Tuples and Functions

Functions can return tuples.

```python
def get_student():
    return ("Rudra", 85)
```

The function returns **one tuple** containing two values.

```python
student = get_student()
```

Now:

```python
student[0]
```

gives:

```python
"Rudra"
```

and:

```python
student[1]
```

gives:

```python
85
```

Mental model:

> Function → returns one tuple → tuple contains multiple values

---

## 14. Combining Tuples with Previous Concepts

Tuples were combined with concepts already learned:

- variables
- assignment
- expressions
- loops
- accumulators
- conditions
- functions
- indexing
- slicing
- membership
- state tracing
- debugging
- problem solving

Example:

```python
def analyze_scores(scores):
    total_score = 0

    for score in scores:
        total_score += score

    return (len(scores), total_score, scores.index(80))
```

---

## 15. Independent Problem Solving

I independently built programs that:

- analyzed tuple length
- checked membership
- found the first index of a value
- counted occurrences
- calculated totals using loops
- returned multiple results inside a tuple
- combined functions and tuples
- solved unfamiliar tuple problems

Example:

```python
def analyze_numbers(numbers):
    total_numbers = 0

    for num in numbers:
        total_numbers += num

    return (
        len(numbers),
        total_numbers,
        7 in numbers,
        numbers.count(12)
    )
```

---

## 16. State Tracing

I practiced predicting how variables and tuples change during execution.

Example:

```python
data = (10, 20, 30)

result = data[1:]

data = data + (40,)
```

The result is:

```python
result
# (20, 30)

data
# (10, 20, 30, 40)
```

The important idea is:

> `result` keeps the value it was assigned, while `data` is later reassigned to a new tuple.
