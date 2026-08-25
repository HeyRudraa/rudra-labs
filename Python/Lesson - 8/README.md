# 🐍 Python Mastery - Lesson 8

## Dictionaries


## 🎯 Lesson Goal

Lesson 8 introduced **Dictionaries** as a foundational Python data structure.

The goal was not simply to learn dictionary syntax, but to understand:

> **Key → Associated Value**

and to learn when a dictionary is the appropriate tool for organizing information.

---

## 🧠 Core Mental Model

Different collections solve different organization problems:

| Data Structure | Main Mental Model |
|---|---|
| **List** | Ordered collection of values |
| **Tuple** | Ordered collection whose elements cannot be reassigned |
| **Dictionary** | Key → associated value |

A dictionary allows information to be accessed through a **meaningful key** instead of relying on a numeric position.

### Example

```python
student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT",
    "marks": 85
}

print(student["course"])
```

The key `"course"` identifies the associated value `"IT"`.

---

# 📚 Concepts Learned

## 1. Why Dictionaries Exist

Learned why position-based access is not always the best way to organize information.

### List

```python
student[3]
```

Requires knowing that the desired value is at index `3`.

### Dictionary

```python
student["marks"]
```

Uses a meaningful key to identify the information.

---

## 2. Creating Dictionaries

### Empty dictionary

```python
student = {}
```

An empty dictionary contains zero entries but the dictionary itself exists.

### Dictionary with entries

```python
student = {
    "name": "Rudra",
    "age": 17
}
```

---

## 3. Adding Dictionary Entries

A new key can be added by assigning a value to it.

```python
student["course"] = "IT"
```

If `"course"` does not already exist, a new key-value entry is created.

---

## 4. Modifying Existing Entries

If the key already exists, assigning to it changes its associated value.

```python
student["age"] = 18
```

Mental model:

```text
Existing key → change associated value
```

Important distinction:

```text
New key      → add entry
Existing key → modify value
```

---

## 5. Dictionary Lookup

Values can be retrieved using their keys.

```python
student["age"]
```

The dictionary finds the key `"age"` and returns its associated value.

---

## 6. Missing Keys and `KeyError`

Trying to access a key that doesn't exist causes a `KeyError`.

```python
student["marks"]
```

if `"marks"` is not present.

The same applies when deleting or popping a missing key.

---

## 7. Dictionary Membership

The `in` operator checks **keys** when used with a dictionary.

```python
student = {
    "name": "Rudra",
    "age": 17
}

print("age" in student)      # True
print("Rudra" in student)    # False
print(17 in student)         # False
```

### Important rule

> **Dictionary membership checks keys, not associated values.**

---

## 8. Removing Entries with `del`

```python
del student["age"]
```

removes the entire key-value entry.

It does not simply change the value.

---

## 9. Removing Entries with `pop()`

```python
removed_age = student.pop("age")
```

`pop()`:

1. Removes the entry.
2. Returns the removed value.

So:

```python
removed_age = student.pop("age")
```

can result in:

```text
student      → entry removed
removed_age  → removed value
```

The returned value does not have to be stored:

```python
student.pop("age")
```

This still removes the entry.

---

# 🔎 Dictionary Views and Iteration

## 10. `.keys()`

```python
student.keys()
```

Provides access to the dictionary's keys.

---

## 11. `.values()`

```python
student.values()
```

Provides access to the dictionary's associated values.

---

## 12. `.items()`

```python
student.items()
```

Provides access to key-value pairs.

Mental model:

```text
.keys()    → keys
.values()  → values
.items()   → key-value pairs
```

---

## 13. Direct Dictionary Iteration

When directly iterating over a dictionary:

```python
for key in student:
    print(key)
```

the loop variable receives the dictionary's keys.

---

## 14. Iterating Through Key-Value Pairs

```python
for key, value in student.items():
    print(key, value)
```

Example:

```text
name Rudra
age 17
```

The loop variables represent:

```text
key   → current key
value → current associated value
```

---

## 15. Iterating Through Values

```python
for value in student.values():
    print(value)
```

Useful when the program only needs the values.

---

# 🛡️ Safe Dictionary Retrieval with `get()`

## 16. Basic `.get()`

```python
student.get("marks")
```

If the key exists:

> returns its associated value.

If the key doesn't exist:

> returns `None` by default.

---

## 17. `.get()` with a Default

```python
student.get("marks", 0)
```

If `"marks"` doesn't exist, `0` is returned.

Mental model:

```text
Key exists?
    ↓
 YES → return actual value
 NO  → return default
```

Example:

```python
student.get("age", 0)       # 17
student.get("marks", 0)     # 0
```

---

## 18. `.get()` Does Not Modify the Dictionary

```python
result = student.get("marks", 0)
```

does not add `"marks": 0` to the dictionary.

It only returns the value or fallback.

---

## 19. `[]` vs `.get()`

### Direct lookup

```python
student["marks"]
```

Missing key:

```text
KeyError
```

### Safe lookup

```python
student.get("marks")
```

Missing key:

```text
None
```

### Safe lookup with fallback

```python
student.get("marks", 0)
```

Missing key:

```text
0
```

---

# 🪆 Nested Dictionaries

A dictionary value can itself be another dictionary.

```python
student = {
    "name": "Rudra",
    "details": {
        "age": 17,
        "course": "IT"
    }
}
```

Nested access:

```python
student["details"]["course"]
```

Execution:

```text
student
  ↓
["details"]
  ↓
inner dictionary
  ↓
["course"]
  ↓
"IT"
```

A value must support the next lookup.

For example, if:

```python
student["details"]
```

returns an integer, trying:

```python
student["details"]["course"]
```

causes a `TypeError`.

---

# 🧩 Mixed Nested Collections

Dictionaries can contain lists and other collections.

Example:

```python
student = {
    "details": {
        "age": 17,
        "skills": ["Python", "HTML"]
    }
}

print(student["details"]["skills"][0])
```

Result:

```text
Python
```

Execution model:

```text
Dictionary
    ↓
Dictionary
    ↓
List
    ↓
Index
```

---

# 🔗 Combining Dictionaries with Previous Concepts

Lesson 8 was intentionally cumulative.

## Dictionaries + Conditions

```python
students = {
    "Rudra": 85,
    "Aarav": 62,
    "Meghshyam": 91
}

for name, score in students.items():
    if score >= 80:
        print(name)
```

Output:

```text
Rudra
Meghshyam
```

---

## Dictionaries + Accumulators

```python
students = {
    "Rudra": 85,
    "Aarav": 62,
    "Meghshyam": 91
}

total_score = 0

for score in students.values():
    total_score += score

print(total_score)
```

Output:

```text
238
```

---

## Dictionaries + Conditions + Counters

```python
scores = {
    "Rudra": 85,
    "Aarav": 72,
    "Meghshyam": 91,
    "Kabir": 64,
    "Neel": 88
}

count_score = 0

for score in scores.values():
    if score >= 80:
        count_score += 1

print(count_score)
```

Output:

```text
3
```

---

# 🧮 Dictionaries + Functions

Built a reusable average-score function:

```python
def find_avg(scores):
    total_score = 0
    count_score = 0

    for score in scores.values():
        total_score += score
        count_score += 1

    return total_score / count_score
```

This demonstrated:

- dictionary parameter
- `.values()`
- loops
- accumulators
- counters
- arithmetic
- return values
- function calls

---

# 🧪 Cumulative Problem Solving

## Finding Top Students

Built a function that returns students scoring 80 or higher:

```python
def get_top_students(scores):
    final_list = []

    for name, score in scores.items():
        if score >= 80:
            final_list += [name]

    return final_list
```

Also experimented with:

```python
final_list.append(name)
```

and learned that for adding one element, `append()` is the clearer and more idiomatic choice.

---

## Inventory Challenge

Built a function to find out-of-stock products:

```python
def check_inventory(inventory):
    out_of_stock = []

    for product_name, quantity in inventory.items():
        if quantity == 0:
            out_of_stock += [product_name]

    return out_of_stock
```

This demonstrated independent selection of:

- `.items()`
- list accumulator
- condition
- loop
- function
- return value

---

## Final `get()` Challenge

Built a safe city lookup:

```python
def show_city(user):
    users_city = user.get("city", "Unknown")

    return users_city
```

This demonstrated understanding of:

- safe dictionary lookup
- default values
- functions
- return values
- no dictionary mutation

---

# 🧠 Data Structure Selection

One of the most important Lesson 8 goals was learning **when to choose a dictionary**, rather than simply learning dictionary syntax.

### List

Choose when the main organization is an **ordered collection**.

```python
days = ["Monday", "Tuesday", "Wednesday"]
```

### Tuple

Choose when you need an **ordered collection whose elements should not be reassigned**.

```python
coordinate = (10, 20)
```

### Dictionary

Choose when information naturally has **meaningful labels/keys and associated values**.

```python
player = {
    "name": "Messi",
    "position": "Forward",
    "age": 39
}
```

The important question is:

> **How does the program need to organize and access the information?**
