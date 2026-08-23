# Python Mastery — Module 1 — Lesson 5

## What I Learned

### 1. Functions

A function is a named, reusable block of code that performs a particular task.

Functions help avoid repeating the same logic and help break programs into smaller responsibilities.

Basic structure:

```python
def greet():
    print("Hello")

greet()
```

Important mental model:

> Definition ≠ Execution

Defining a function does not execute its body. The body executes when the function is called.

---

### 2. Parameters and Arguments

A **parameter** is the name/placeholder used by a function to receive a value.

An **argument** is the value supplied when calling the function.

```python
def greet(name):
    print("Hello", name)

greet("Rudra")
```

- `name` → parameter
- `"Rudra"` → argument

Mental model:

> Argument → Parameter → Function execution

---

### 3. Multiple Parameters

Functions can receive multiple parameters.

```python
def calculate(a, b):
    result = a + b
    print(result)

calculate(5, 3)
calculate(10, 2)
```

Each function call executes the function body again with the new argument values.

---

### 4. `return`

`return` sends a value back to the code that called the function.

```python
def add(a, b):
    result = a + b
    return result

x = add(4, 6)
print(x)
```

Here, `x` becomes `10`.

Important distinction:

> `print()` → displays a value  
> `return` → sends a value back to the caller

A function that reaches the end without returning a value returns `None`.

Example:

```python
def test():
    print("Hello")

result = test()
print("result =", result)
```

Output:

```text
Hello
result = None
```

---

### 5. `return` Ends the Current Function Execution

When Python reaches `return`, the current function execution ends immediately.

```python
def test():
    print("A")
    return 10
    print("B")

x = test()
print(x)
```

Output:

```text
A
10
```

`print("B")` never executes.

---

### 6. Conditional Returns

A function can return different values depending on a condition.

```python
def check(number):
    if number > 10:
        return "Big"

    return "Small"
```

The condition determines which return is reached.

---

### 7. Local Variables and Scope

A variable created inside a function is local to that function.

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Output:

```text
20
10
```

The two `x` variables are separate in this situation.

Important mental model:

> A variable name inside a function is not automatically the same variable as a name outside the function.

Parameters are also local to the function.

```python
x = 100

def change(x):
    x = x + 50
    return x

result = change(10)

print("result =", result)
print("x =", x)
```

Output:

```text
result = 60
x = 100
```

---

### 8. Reading an Outer Variable

If a function does not have its own local variable with a particular name, it can access a suitable variable from an outer/enclosing scope.

```python
x = 10

def test():
    print(x)

test()
```

Output:

```text
10
```

A function does not search unrelated functions for their local variables.

---

### 9. Nested Functions

A function can be defined inside another function.

```python
def outer():
    x = 50

    def inner():
        print(x)

    inner()

outer()
```

Output:

```text
50
```

`inner()` can access `x` from its enclosing scope.

Important distinction:

- A separate function does not automatically get access to another function's local variables.
- A nested function can access suitable values from its enclosing scope.

---

### 10. Functions Can Call Other Functions

One function can call another function.

```python
def greet():
    print("Hello")

def start():
    greet()

start()
```

Execution conceptually:

```text
start()
  ↓
greet()
  ↓
print("Hello")
  ↓
greet() finishes
  ↓
start() finishes
```

---

## Function Decomposition

Functions can help break a larger problem into smaller responsibilities.

For example:

```python
def calculate_total(a, b, c):
    return a + b + c

def calculate_percentage(total):
    return total / 3

def check_result(percentage):
    if percentage >= 40:
        return "Pass"

    return "Fail"
```

The important idea is:

> Problem → smaller responsibilities → functions

A function does not have to represent every tiny operation. The goal is reasonable decomposition and clear responsibility.

---

## Boundary Conditions

Functions should be tested at important boundaries.

Example:

```python
def check_result(marks):
    if marks >= 40:
        return "Pass"

    return "Fail"
```

Testing `40` is important because:

```python
40 >= 40
```

is `True`.

Boundary testing helped verify that the condition matches the requirement.

---

# Practical Programs Built

## 1. `is_even()`

```python
def is_even(num):
    if num % 2 == 0:
        return "Even"

    return "Odd"

print(is_even(8))
print(is_even(7))
```

---

## 2. `max_of_three()`

```python
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(max_of_three(10, 25, 7))
print(max_of_three(50, 20, 80))
print(max_of_three(5, 5, 3))
```

Also tested equality cases such as:

```python
max_of_three(5, 3, 5)
max_of_three(5, 5, 5)
```

---

## 3. `check_result()`

```python
def check_result(marks):
    if marks >= 40:
        return "Pass"

    return "Fail"

print(check_result(40))
print(check_result(20))
print(check_result(90))
```

---

## 4. Student Result Function

```python
def check_result(marks1, marks2, marks3):
    avg_marks = (marks1 + marks2 + marks3) / 3

    if avg_marks >= 40:
        return "Pass"

    return "Fail"

print(check_result(40, 40, 40))
print(check_result(20, 60, 24))
print(check_result(90, 89, 96))
```

---

## 5. `ticket_price()`

```python
def ticket_price(age):
    if age < 5:
        return "Free"

    elif age < 18:
        return "100"

    elif age < 110:
        return "200"

    else:
        return "Invalid Age"

ticket_price(3)
ticket_price(10)
ticket_price(17)
ticket_price(25)
ticket_price(30)
```

This exercise also introduced thinking about **input validation and edge cases** beyond the original requirements.

---

## 6. `calculate_bill()`

```python
def calculate_bill(units):
    if units <= 100:
        return "Low Usage"

    elif units <= 300:
        return "Medium Usage"

    else:
        return "High Usage"

print(calculate_bill(100))
print(calculate_bill(101))
print(calculate_bill(300))
print(calculate_bill(301))
```

This demonstrated boundary reasoning:

```text
100 → Low Usage
101 → Medium Usage
300 → Medium Usage
301 → High Usage
```

---
