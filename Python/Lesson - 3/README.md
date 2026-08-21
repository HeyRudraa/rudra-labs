# Lesson 3 — Conditional Logic

## What I Learned

Lesson 3 focused on **conditional logic and control flow** — how a Python program makes decisions and chooses what code to execute.

The core mental model developed was:

> **Condition → Evaluation → Result → Execution Path**

---

## Conditions and Boolean Results

A condition is an expression that can be evaluated to determine whether something is true or false.

Example:

```python
age >= 18
```

This is a **comparison expression**.

Python evaluates it and produces a Boolean value:

```python
True
```

or:

```python
False
```

Important distinction:

- The expression is `age >= 18`.
- Evaluating the expression produces a Boolean value.
- `True` and `False` are actual Boolean values of type `bool`.

---

## Expression Evaluation

A comparison is still an expression.

For example:

```python
10 + 5
```

evaluates to:

```python
15
```

while:

```python
10 > 5
```

evaluates to:

```python
True
```

The general mental model is:

> **Expression → evaluation → resulting value**

This connects conditional logic directly to the evaluation concepts learned previously.

---

## `if`

`if` allows a program to execute code conditionally.

```python
if age >= 18:
    print("Adult")
```

Python evaluates the condition first.

- If it is true, the `if` suite executes.
- If it is false, the suite is skipped.

---

## `else`

`else` provides the alternative branch when the `if` condition is false.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

For one `if/else` decision:

> Exactly one branch executes.

The `else` itself is not a condition. It provides the alternative branch.

---

## `elif`

`elif` allows multiple connected conditions to be checked.

```python
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

Python evaluates the conditions from top to bottom.

Once it finds a true condition:

1. That branch executes.
2. Remaining `elif` conditions are not evaluated.
3. The `else` is not executed.

### Important distinction

Multiple independent `if` statements are different from an `if/elif/else` chain.

- Multiple `if` statements are independent decisions.
- `if/elif/else` is one connected decision chain.

---

## Indentation and Suites

Python uses indentation to define the structure of conditional code.

```python
if score >= 50:
    print("Passed")
    print("Good job")

print("Result checked")
```

The two indented statements belong to the `if` suite.

The final `print()` does not belong to the `if`.

A blank line does not change the structure of a Python block. Indentation does.

---

## Nested Conditions

A conditional statement can contain another conditional statement.

```python
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")
```

The outer condition decides whether the inner decision is reached.

If the outer condition is false, the entire outer suite is skipped, including the inner `if`.

Indentation determines which `else` belongs to which `if`.

---

## Logical Operator: `and`

`and` combines conditions when all requirements must be satisfied.

```python
if age >= 18 and has_id:
    print("Entry allowed")
```

The basic truth behavior is:

```text
True and True   → True
True and False  → False
False and True  → False
False and False → False
```

### Short-circuit behavior

Python evaluates `and` from left to right.

If it encounters a false operand, the overall result cannot become true, so evaluation can stop.

Conceptually:

```text
False and anything → False
True and ...       → continue
```

---

## Logical Operator: `or`

`or` is used when at least one condition is sufficient.

```python
if age >= 18 or has_permission:
    print("Entry allowed")
```

Basic truth behavior:

```text
True or True   → True
True or False  → True
False or True  → True
False or False → False
```

### Short-circuit behavior

Python evaluates `or` from left to right.

If it encounters a true operand, the overall result is already known to be true, so it can stop evaluating further operands.

Conceptually:

```text
True or anything  → True
False or ...      → continue
```

---

## Logical Operator: `not`

`not` negates a Boolean value.

```text
not True  → False
not False → True
```

Example:

```python
if not is_banned:
    print("Entry allowed")
```

Important terminology:

> `not` negates the Boolean value produced by an expression.

---

## Logical Operator Precedence

When `not`, `and`, and `or` appear together, their logical precedence is:

```text
not
and
or
```

So:

```python
age >= 18 or has_permission and not is_banned
```

is interpreted conceptually as:

```text
age >= 18 or (has_permission and (not is_banned))
```

not:

```text
(age >= 18 or has_permission) and not is_banned
```

Understanding precedence prevents incorrect reasoning about compound conditions.

---

## Boundary Conditions

Small comparison differences can change program behavior.

For example:

```python
marks > 50
```

does not include `50`.

But:

```python
marks >= 50
```

does include `50`.

Important comparison operators:

```text
>   greater than
>=  greater than or equal to
<   less than
<=  less than or equal to
==  equal to
!=  not equal to
```

A boundary value is the value where the outcome changes.

Boundary testing should include:

- a value below the boundary
- the boundary itself
- a value above the boundary

Example:

```text
999  → below
1000 → boundary
1001 → above
```

---

## Assignment vs Equality Comparison

These operators have different purposes:

```python
age = 18
```

`=` performs assignment.

```python
age == 18
```

`==` compares values for equality.

Therefore:

```python
if age = 18:
```

is invalid Python syntax because assignment and equality comparison are different operations.

---

## Conditional Logic and Previous Conditions

Earlier conditions can establish information for later branches.

Example:

```python
if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")
```

When Python reaches:

```python
elif age <= 17:
```

we already know the first condition was false.

Therefore, we already know:

```text
age >= 13
```

Combined with:

```text
age <= 17
```

the effective range becomes:

```text
13 <= age <= 17
```

This means conditions do not always need to repeat information already established by previous branches.

---

## Truthiness and Falsiness

A condition does not always have to literally contain a Boolean value.

Python can evaluate other values in a **Boolean context** and determine whether they are truthy or falsy.

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("No name")
```

The empty string is not literally the Boolean `False`, but it is **falsy**.

Likewise:

```python
name = "Rudra"
```

is a string, not the Boolean `True`, but a non-empty string is **truthy**.

### Important distinction

**Boolean value:**

```python
True
False
```

**Truthy/falsy behavior:**

```text
"hello" → truthy
10       → truthy
[]       → falsy
""       → falsy
0        → falsy
-1       → truthy
```

So:

> A value can be truthy without literally being the Boolean `True`.

---

## Truthiness of Important Values

Important beginner-level cases demonstrated:

```text
0        → falsy
non-zero integer → truthy

""       → falsy
non-empty string → truthy

[]       → falsy
non-empty list → truthy
```

For example:

```text
[]       → falsy
[0]      → truthy
```

`[0]` is truthy because the list is non-empty. Python is evaluating the truthiness of the list itself, not the truthiness of each element inside it.

Similarly:

```text
""       → falsy
"0"      → truthy
```

because `"0"` is a non-empty string.

Negative integers are also truthy:

```text
-1   → truthy
-50  → truthy
```

The important integer rule learned was:

> **Zero is falsy; non-zero integers are truthy.**

---

## `bool()`

`bool()` can be used to obtain the Boolean truth value of a value.

Examples:

```python
bool(0)
# False

bool(10)
# True

bool("")
# False

bool("Python")
# True

bool([])
# False

bool([0])
# True
```

This reinforced the distinction between an actual Boolean value and the truthiness of another type.

---

## Debugging Conditional Logic

Conditional debugging was practiced by:

1. Reading the conditions.
2. Evaluating them in order.
3. Identifying which branch is reached.
4. Checking whether later conditions are skipped.
5. Finding overlapping or incorrectly ordered conditions.
6. Testing boundary values.
7. Correcting the decision structure.

A major debugging lesson was:

> **A condition can be individually correct but still produce incorrect program behavior because of its position in the decision chain.**

For example, a broad condition such as:

```python
marks >= 50
```

placed before:

```python
marks >= 75
```

can prevent the more specific condition from ever being reached.

---

## Practical Programs Built

Conditional logic was independently applied to small programs including:

### Age Classification

```text
below 13 → Child
13–17 → Teenager
18+ → Adult
```

### Movie Entry

```text
18+ → allowed
under 18 + parental permission → allowed
otherwise → denied
```

### Shopping Discount

```text
5000+ → 20%
2000–4999 → 10%
below 2000 → 0%
```

### Grade Classification

```text
90+ → A
80–89 → B
70–79 → C
60–69 → D
below 60 → F
```

### Player Rank Classification

```text
100+ → Legend
75–99 → Elite
50–74 → Pro
25–49 → Rookie
below 25 → Beginner
```

These programs required translating requirements into conditions, ordering conditions correctly, handling boundaries, and predicting outputs.

---

## What I Demonstrated

### Prediction

I demonstrated the ability to:

- predict Boolean results
- trace `if/elif/else`
- determine which branch executes
- identify which conditions are skipped
- trace nested conditions
- reason about `and`, `or`, and `not`
- reason about truthiness
- predict boundary behavior

### Construction

I independently created conditional programs from written requirements instead of only modifying provided examples.

### Debugging

I successfully identified:

- incorrect condition ordering
- overlapping conditions
- incorrect boundary operators
- incorrect use of independent `if` statements
- unnecessary or incorrect branches
- structural differences between independent decisions and connected decision chains

### Reasoning

The strongest demonstrated mental model became:

> **Evaluate the condition → obtain its result/truth value → choose the execution path → execute only the selected branch.**

---

## Main Strengths

- Strong expression tracing
- Strong Boolean reasoning
- Strong `if/elif/else` reasoning
- Strong boundary reasoning
- Strong debugging of conditional logic
- Good ability to translate requirements into code
- Good understanding of nested control flow
- Good understanding of short-circuit behavior
- Good transfer from examples to unfamiliar problems

## Main Weakness

### Technical terminology and precision

The conceptual reasoning was generally ahead of the vocabulary.

Examples of terminology that needed refinement:

- `elif` is a keyword, not a function.
- A condition is evaluated; it is not "executed."
- `else` is a branch, not a condition.
- `True`/`False` are Boolean values.
- Truthy/falsy describes how values behave in Boolean contexts.
- `10` is not literally `True`; it is an integer that is truthy.

The concepts were corrected successfully during the lesson.

---
