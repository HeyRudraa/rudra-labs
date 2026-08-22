# Lesson 4 — Loops & Repetition

## What I Learned

Lesson 4 focused on **loops and repetition** — how a Python program can repeatedly execute code, process values one by one, control repeated execution, and solve problems that would otherwise require unnecessary duplicated code.

The core mental models developed were:

> **While:** Condition → Evaluation → Body → State Change → Re-check → Stop

> **For:** Get next item → Execute body → Get next item → Continue or Stop

---

## Why Loops Exist

Without loops, repetitive work would require writing the same statements again and again.

For example:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

A loop allows the programmer to describe the repetition instead of manually duplicating the work.

Loops also make programs easier to modify. Changing a starting value, ending condition, or repetition rule can be done in one place instead of changing many duplicated statements.

---

## `while` Loops

A `while` loop repeats a block of code while its condition evaluates to `True`.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

The execution model developed was:

```text
Check condition
      ↓
   True?
      ↓
Execute loop body
      ↓
Change loop state
      ↓
Check condition again
```

If the condition is initially `False`, the loop body executes zero times.

### Loop State

A loop often depends on a value that changes between iterations.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Here:

- `count = 1` establishes the initial state.
- `count <= 5` is the repetition condition.
- `count += 1` changes the state.

The state change allows the loop to eventually reach a condition that evaluates to `False`.

### Infinite Loops

If the state never changes in a way that can make the condition `False`, the loop can continue indefinitely.

For example:

```python
count = 1

while count <= 5:
    print(count)
```

`count` remains `1`, so:

```text
1 <= 5 → True
1 <= 5 → True
1 <= 5 → True
...
```

This creates an infinite loop.

---

## `for` Loops

A `for` loop processes items one at a time.

Example:

```python
for fruit in ["apple", "banana", "mango"]:
    print(fruit)
```

The mental model developed was:

```text
Take next item
      ↓
Store it in the loop variable
      ↓
Execute the loop body
      ↓
Take the next item
```

The loop variable represents the **current item** being processed during each iteration.

---

## Iteration

Each individual pass through a loop is an **iteration**.

For example:

```python
for fruit in ["apple", "banana", "mango"]:
    print(fruit)
```

has three iterations:

```text
Iteration 1 → fruit = "apple"
Iteration 2 → fruit = "banana"
Iteration 3 → fruit = "mango"
```

A `for` loop can also iterate through a string:

```python
for character in "Rudra":
    print(character)
```

Output:

```text
R
u
d
r
a
```

This demonstrated that a string can provide its characters one at a time to a `for` loop.

---

## `range()`

`range()` was used to generate controlled sequences of numbers for `for` loops.

### `range(stop)`

```python
range(5)
```

produces:

```text
0
1
2
3
4
```

The stop value is excluded.

### `range(start, stop)`

```python
range(2, 7)
```

produces:

```text
2
3
4
5
6
```

The starting value is included and the stopping value is excluded.

### `range(start, stop, step)`

```python
range(2, 10, 2)
```

produces:

```text
2
4
6
8
```

The step controls how much the generated value changes between iterations.

### Negative Steps

A negative step moves downward:

```python
range(5, 0, -1)
```

produces:

```text
5
4
3
2
1
```

The direction of the step must make sense with the start and stop values.

For example:

```python
range(0, 5, -1)
```

is valid but empty because the sequence moves downward from `0` while the stop boundary is `5`.

### Empty Ranges

```python
range(5, 5)
```

contains no values.

An empty `range()` does not cause an error; it simply causes the loop body to execute zero times.

### Important Boundary Rule

> **The start value is included; the stop value is excluded.**

This rule was repeatedly tested because it is important when predicting loop behavior.

---

## `break`

`break` immediately terminates the current loop.

Example:

```python
for number in range(1, 21):
    print(number)

    if number % 7 == 0:
        break
```

The loop prints through `7` and then stops.

The important execution model is:

```text
Condition becomes True
      ↓
break executes
      ↓
Current loop terminates
      ↓
Program continues after the loop
```

`break` was used for problems where the program needed to find something and then stop searching.

---

## `continue`

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

Example:

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)
```

This prints the odd numbers.

The execution model is:

```text
Current iteration
      ↓
continue
      ↓
Skip remaining code
      ↓
Next iteration
```

### Important `continue` Edge Case

`continue` can cause an infinite loop if it skips the code responsible for changing the loop state.

For example:

```python
x = 0

while x < 5:
    if x == 2:
        continue

    x += 1
```

When `x` becomes `2`, `continue` executes before `x += 1`.

Therefore `x` remains `2`, and the same condition keeps being reached.

---

## `break` vs `continue`

The difference was established as:

```text
break
→ Stop the entire loop

continue
→ Skip the current iteration and keep looping
```

Their position inside a loop can significantly change program behavior.

---

## Loops + Conditional Logic

Loops can be combined with conditions to make decisions for every iteration.

Example:

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

The loop processes each number and the condition determines which values qualify.

This creates a useful pattern:

```text
Loop
 ↓
Process current value
 ↓
Evaluate condition
 ↓
Perform action if condition is satisfied
```

Conditions can also combine multiple requirements using logical operators such as `and`.

Example:

```python
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print(number)
```

---

## Filtering Values

Loops can be used to filter values based on conditions.

For example:

```python
for number in range(1, 21):
    if number % 3 != 0:
        print(number)
```

Only values that satisfy the condition are processed by the `print()` statement.

`continue` can also be used when unwanted values should be skipped before the remaining work in the iteration.

---

## Nested Loops

A loop can contain another loop.

Example:

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

The important execution rule is:

> **For every iteration of the outer loop, the entire inner loop completes its iterations.**

Conceptually:

```text
i = 1
    j = 1
    j = 2

i = 2
    j = 1
    j = 2

i = 3
    j = 1
    j = 2
```

The total number of inner executions depends on both loop sizes.

---

## Nested Loops and Patterns

Nested loops can be used to generate structured output.

Example:

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

This produces:

```text
*
* *
* * *
* * * *
```

The outer loop controls the rows while the inner loop controls how many items are produced in each row.

This also demonstrated how an outer-loop value can determine the number of inner-loop iterations.

---

## Accumulator Pattern

An accumulator stores a running result while a loop processes values.

Example:

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)
```

The value develops as:

```text
0 → 1 → 3 → 6 → 10 → 15
```

The core pattern is:

> **Previous result + current value → updated result**

The accumulator was used to calculate sums, including the sum of even numbers.

---

## Counter Pattern

A counter tracks how many times something happens.

Example:

```python
count = 0

for number in range(1, 21):
    if number % 2 == 0:
        count += 1

print(count)
```

The important distinction is:

```text
Counter
→ How many qualifying values?

Accumulator
→ What is the combined result of their values?
```

For example:

```python
count += 1
```

counts an occurrence, while:

```python
total += number
```

adds the actual value to a running total.

---

## Counter + Accumulator + `break`

These patterns can be combined to solve more realistic problems.

Example:

```python
count = 0
total = 0

for number in range(1, 101):
    if number % 3 == 0:
        print(number)
        count += 1

        if count == 4:
            break
```

This demonstrates:

```text
Filter
 ↓
Process
 ↓
Count
 ↓
Check stopping requirement
 ↓
Break when required
```

---

## Edge Cases and Boundaries

Important loop boundaries practiced included:

- zero iterations
- one iteration
- equal start and stop values
- excluded stop values
- positive steps
- negative steps
- ranges moving in the wrong direction
- conditions that are initially false
- conditions that never become false
- state changes that happen before or after a condition
- `break` and `continue` placement

The main lesson was:

> **Small changes in boundaries or statement order can completely change loop behavior.**

---

## Debugging Loops

Loop debugging was practiced by:

1. Reading the loop condition or iteration source.
2. Tracing the current value.
3. Checking what the body does.
4. Checking how state changes.
5. Determining where control flow goes next.
6. Identifying why a loop stops or fails to stop.
7. Testing the corrected behavior.

A major debugging lesson was:

> **A loop bug is often caused not by one statement being individually wrong, but by the interaction and position of statements inside the loop.**

Examples included:

- missing state updates
- infinite loops
- `continue` skipping state changes
- `break` occurring before required work
- unreachable code after `continue`
- incorrect `range()` boundaries
- incorrect loop termination logic

---

## Practical Programs Built

Loop-based programs were independently constructed to:

- Find numbers divisible by both 3 and 5
- Skip even numbers and stop at 15
- Find the first number divisible by both 4 and 7
- Calculate the sum of even numbers from 1 to 20
- Count numbers divisible by both 3 and 5
- Find the first number divisible by 4 but not 6
- Print the first four numbers divisible by 3
- Sum the first five numbers divisible by either 3 or 5, but not both
- Find and sum the first three numbers divisible by 4 but not 6

These problems required combining loops, conditions, counters, accumulators, and control statements.

---

## What I Demonstrated

### Prediction

I demonstrated the ability to:

- Predict loop output before execution
- Trace individual iterations
- Determine when conditions are evaluated
- Predict final variable values
- Reason about `break` and `continue`
- Predict `range()` boundaries
- Trace nested-loop execution
- Identify infinite-loop behavior

### Construction

I independently wrote programs using:

- `while`
- `for`
- `range()`
- `if`
- `and`
- `or`
- `not`
- `%`
- `break`
- `continue`
- counters
- accumulators
- nested loops

### Debugging

I successfully identified and corrected:

- Missing loop state updates
- Infinite loops
- Incorrect `break` placement
- Incorrect `continue` placement
- Unreachable statements after `continue`
- `range()` boundary mistakes
- Incorrect stopping logic
- Incorrect execution order

### Problem Solving

I demonstrated the ability to translate written requirements into working loop-based programs and apply the same concepts to unfamiliar problems.

---
