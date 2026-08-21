# Values, Variables, Expressions, and Operators

## 1. Values and Data

Python programs work with values.

Examples:

```python
17
85
"Rudra"
"Python"
10.5
```

Values can have different types:

- `17` → `int`
- `"17"` → `str`
- `10.5` → `float`

Values that look similar can still have different types:

```python
17
"17"
```

The first is an integer and the second is a string.

---

## 2. Variables

A variable name allows a program to refer to a value.

```python
age = 17
```

Basic mental model:

**Name → Value/Object**

Variables give values meaningful names so they can be used later.

---

## 3. Assignment

`=` is the **assignment operator**.

```python
age = 17
```

Assignment is not mathematical equality.

It means:

**Evaluate the right-hand side → assign the resulting value to the name on the left.**

Example:

```python
total = price + tax
```

Python evaluates the expression first and then assigns the resulting value to `total`.

### Mental Model

**Name = Expression → Evaluate → Resulting Value → Assignment**

---

## 4. Reassignment

A variable can be assigned a new value.

```python
age = 17
age = 18
```

After the second assignment:

```text
age → 18
```

Reassignment changes what the name is associated with.

---

## 5. Assigning One Variable From Another

A variable can be used when assigning another variable.

```python
x = 10
y = x
```

At the time `y = x` executes, Python evaluates the current value of `x` and assigns that value to `y`.

```python
x = 10
y = x

x = 20
```

Now:

```text
x → 20
y → 10
```

Changing `x` later does not automatically change `y`.

### Mental Model

**Evaluate the current value → assign that value to the new name**

---

## 6. `print()`, `sep`, `end`, and `\n`

`print()` displays values and variables.

```python
name = "Rudra"
age = 17

print(name)
print(age)
```

Output:

```text
Rudra
17
```

Multiple arguments can be printed:

```python
print("Rudra", "Python")
```

Output:

```text
Rudra Python
```

### `sep`

`sep` controls what is placed between multiple arguments.

```python
print("Age", 17, sep=": ")
```

Output:

```text
Age: 17
```

### `end`

`end` controls what is added after the output.

```python
print("Hello", end=" ")
print("Rudra")
```

Output:

```text
Hello Rudra
```

By default, `print()` ends with a newline.

### `\n`

`\n` represents a newline character inside a string.

```python
print("Hello\nRudra")
```

Output:

```text
Hello
Rudra
```

---

## 7. Strings and Quotes

Strings can use single or double quotes:

```python
'Rudra'
"Rudra"
```

One type of quote can appear inside a string delimited by the other:

```python
message = 'Rudra said "Python" is fun'
```

```python
message = "Rudra said 'Python' is fun"
```

### Escaping Quotes

When the same quote character used to delimit a string needs to appear inside the string, it can be escaped with `\`.

```python
message = "Rudra said, \"Python's variables are powerful!\""
```

---

## 8. Expressions

An **expression** is something Python can evaluate to produce a value.

```python
10 + 5
```

produces:

```text
15
```

Example:

```python
age = 17
next_age = age + 1
```

Python evaluates:

```text
17 + 1
→ 18
```

and assigns `18` to `next_age`.

### Mental Model

**Expression → Evaluation → Resulting Value**

---

## 9. Operators and Operands

Operators perform operations on operands.

Example:

```python
a + b
```

- `a` → operand
- `+` → operator
- `b` → operand

Operators practiced:

```text
+   Addition / string concatenation
-   Subtraction
*   Multiplication / string repetition
/   True division
//  Floor division
%   Modulo / remainder
```

---

## 10. Arithmetic Expressions

Variables can be combined with operators to calculate new values.

```python
a = 10
b = 5

result = a + b
```

The expression:

```python
a + b
```

becomes:

```text
10 + 5
→ 15
```

---

## 11. Operator Precedence

When multiple operators appear in an expression, Python follows precedence rules.

Basic order practiced:

**Parentheses → Multiplication/Division → Addition/Subtraction**

Example:

```python
result = 10 + 3 * 2
```

Evaluation:

```text
3 * 2
→ 6

10 + 6
→ 16
```

---

## 12. Parentheses and Grouping

Parentheses group an expression and cause that part to be evaluated first.

```python
result = (10 + 3) * 2
```

Evaluation:

```text
10 + 3
→ 13

13 * 2
→ 26
```

Without parentheses:

```python
10 + 3 * 2
```

produces:

```text
16
```

---

## 13. Evaluation of Equal-Precedence Operators

When addition and subtraction appear together, they have the same precedence and are evaluated from left to right.

```python
10 + 6 - 4
```

Evaluation:

```text
10 + 6
→ 16

16 - 4
→ 12
```

---

## 14. Evaluation Happens When Python Reaches the Expression

An expression assigned to a variable is evaluated when Python reaches that assignment.

```python
x = 10
y = x + 5
x = 100
```

When `y = x + 5` executes, `x` is `10`.

Therefore:

```text
10 + 5
→ 15
```

So:

```text
y → 15
```

Later changing `x` to `100` does not change `y`.

### Mental Model

**Evaluate now → Store resulting value**

The expression is not stored as a permanently updating formula.

---

## 15. Addition vs String Concatenation

The `+` operator behaves according to the types of its operands.

Integers:

```python
10 + 5
```

produce:

```text
15
```

Strings:

```python
"Hello" + " Rudra"
```

produce:

```text
Hello Rudra
```

With strings, `+` performs **concatenation**.

---

## 16. String Repetition

The `*` operator can repeat a string when combined with an integer.

```python
"Ha" * 3
```

produces:

```text
HaHaHa
```

The order can also be reversed:

```python
3 * "Ha"
```

and produces the same result.

---

## 17. Type Compatibility and `TypeError`

Different types cannot always be used together.

For example:

```python
10 + "5"
```

raises a `TypeError`.

The problem is:

```text
int + str
```

Python cannot perform normal numerical addition between an integer and a string.

---

## 18. String and Integer Multiplication

A special mixed-type operation is:

```python
"300" * 4
```

This is valid and repeats the string:

```text
300300300300
```

The reverse also works:

```python
4 * "300"
```

This shows that mixed types do not automatically mean an operation is invalid.

The operator and operand types together determine what Python can do.

---

## 19. Type Conversion

Values can be converted to another type using conversion functions.

### `str()`

```python
age = 17
text_age = str(age)
```

Now:

```text
age → 17 → int
text_age → "17" → str
```

### `int()`

```python
quantity = "3"
quantity_as_int = int(quantity)
```

Now:

```text
quantity → "3" → str
quantity_as_int → 3 → int
```

Conversion can also happen inside an expression:

```python
total = price * int(quantity)
```

This converts the value for that expression without reassigning the original variable.

---

## 20. `type()`

`type()` can inspect the type of a value.

```python
age = 17
print(type(age))
```

Output:

```text
<class 'int'>
```

For a string:

```python
text_age = "17"
print(type(text_age))
```

Output:

```text
<class 'str'>
```

`type()` can also inspect expressions:

```python
print(type(10 + 5))
```

Python first evaluates:

```text
10 + 5
→ 15
```

Then checks the type:

```text
<class 'int'>
```

### Mental Model

**Expression → Resulting Value → `type()` → Type**

---

## 21. Division, Floor Division, and Modulo

### `/` — True Division

```python
17 / 5
```

produces:

```text
3.4
```

The result is a `float`.

### `//` — Floor Division

```python
17 // 5
```

produces:

```text
3
```

### `%` — Modulo

```python
17 % 5
```

produces:

```text
2
```

because:

```text
5 × 3 = 15
17 - 15 = 2
```

The result is the remainder.

---

## 22. Types of Division Results

```python
a = 17
b = 5

print(a / b)
print(type(a / b))

print(a // b)
print(type(a // b))

print(a % b)
print(type(a % b))
```

Results:

```text
3.4
<class 'float'>
3
<class 'int'>
2
<class 'int'>
```

---

## 23. Real-World Uses of `//` and `%`

### Splitting a Total

```python
total = 1250
people = 4

share = total // people
remainder = total % people
```

Results:

```text
share → 312
remainder → 2
```

### Converting Seconds

```python
seconds = 367

minutes = seconds // 60
remaining_seconds = seconds % 60
```

Results:

```text
minutes → 6
remaining_seconds → 7
```

Meaning:

**367 seconds = 6 minutes and 7 seconds.**

---

## 24. Augmented Assignment

Python provides shorter forms for common reassignment operations.

```python
score += 5
```

is equivalent at this level to:

```python
score = score + 5
```

Other examples:

```python
score -= 2
score *= 3
```

Example:

```python
points = 10

points += 5
points *= 2
points -= 4
```

Evaluation:

```text
10
→ 15
→ 30
→ 26
```

These are called **augmented assignment operators**.

---

## 25. Debugging Type Errors

We practiced identifying errors caused by incompatible types.

Example:

```python
price = 500
quantity = "3"

total = price * int(quantity)
```

Here:

```text
"3"
→ int("3")
→ 3
```

so:

```text
500 * 3
→ 1500
```

### Debugging Mental Model

**Identify the failing expression → Inspect operand types → Determine the incompatible operation → Fix the types → Re-evaluate**

---

## 26. Debugging Logic Errors

A program can be syntactically valid and still calculate the wrong result.

Example:

```python
price = 500
quantity = 2
discount = 100

total = price + quantity - discount
```

The program can execute, but the logic is wrong.

The correct relationship is:

```python
total = price * quantity - discount
```

because quantity represents the number of items.

This demonstrates:

**A program can execute successfully and still be logically incorrect.**

---

## 27. Building Calculations Step by Step

Programs can build calculations through intermediate values.

```python
price = 250
quantity = 3
discount = "50"

int_discount = int(discount)

sub_total = price * quantity
total = sub_total - int_discount
```

Dependency:

```text
price + quantity
      ↓
subtotal
      ↓
discount conversion
      ↓
final total
```

Results:

```text
subtotal → 750
total → 700
```

Using meaningful intermediate variables can make a calculation easier to understand and debug.

---

## 28. Student Marks Calculation

A student marks calculation can be built from source values:

```python
sub_math = 85
sub_python = 92
sub_science = 78

total_marks = sub_math + sub_python + sub_science
average_marks = total_marks / 3
```

Results:

```text
total_marks → 255
average_marks → 85.0
```

The total is calculated from the subject values instead of being manually hard-coded.

This means changing a subject mark automatically changes the total and average.

---

## 29. Key Mental Models

### Variable

**Name → Current Value/Object**

### Assignment

**Name = Expression → Evaluate → Assign Result**

### Reassignment

**Reassigning a name changes its current association.**

### Expression

**Expression → Evaluation → Resulting Value**

### Operator

**Operator + Operands → Operation → Result**

### Type

**Type influences which operations are valid and how values behave.**

### Type Conversion

**Original Value → Conversion Function → New Value**

### Debugging

**Observe → Identify → Explain → Correct → Test**

### Program Calculation

**Input Values → Expressions → Intermediate Results → Final Result → Output**

---
