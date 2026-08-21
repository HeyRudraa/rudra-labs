# What Is Programming, and What Is Python?

## 1. What Is Programming?

Programming is the process of creating and organizing precise instructions to achieve a goal or solve a problem.

A large goal can be broken into smaller steps that a computer can execute.

### Mental Model

**Goal → Smaller Steps → Precise Instructions → Correct Order → Execution → Result**

---

## 2. What Is a Program?

A program is a set of instructions that a computer can execute to perform a task.

A program is not the same thing as the goal:

- **Goal:** What we want to achieve.
- **Program:** The instructions used to achieve it.

---

## 3. Why Do Programming Languages Exist?

Humans naturally communicate using languages such as English and Marathi, while computers require instructions in forms they can process and execute.

Programming languages provide humans with a structured way to express instructions for computers.

### Mental Model

**Human intention → Programming language → Computer execution → Result**

---

## 4. What Is Python?

Python is a **general-purpose programming language**.

It allows programmers to express instructions in a relatively readable and understandable form.

The important point here is Python's role as a programming language, rather than learning its application areas in depth.

---

## 5. Programming vs Python

Programming and Python are not the same thing.

- **Programming:** The broader skill and process of solving problems through instructions.
- **Python:** One programming language used to express those instructions.

Programming concepts can transfer between languages even when their syntax is different.

Knowing Python syntax alone does not automatically make someone a strong programmer. Understanding the problem, requirements, logic, order of operations, and required steps is more fundamental.

---

## 6. Precision of Instructions

A computer cannot reliably fill in missing details of an instruction the way a human can.

For example:

> "Make a sandwich."

is less precise than instructions specifying the ingredients, quantities, and actions.

This demonstrates an important principle:

> **Computer instructions need to be precise and unambiguous enough for the intended behavior.**

---

## 7. Order of Execution

The order of instructions can affect the result of a program.

We practiced reasoning about instructions executing from top to bottom.

Example:

```python
print("Start")
print("Middle")
print("End")
```

Output:

```text
Start
Middle
End
```

A later instruction may also depend on something being done earlier.

For example, a value should be available before the program tries to use it.

### Mental Model

**Earlier instruction → Result/State → Later instruction can use it**

---

## 8. Code, Execution, and Output

We distinguished between the instructions written by the programmer and the result produced when those instructions execute.

Example:

```python
print("Hello")
```

- `print("Hello")` → Python code/instruction
- `Hello` → output

### Mental Model

**Code → Execution → Output**

---

## 9. Basic `print()` Understanding

`print()` was used to practice predicting program behavior.

```python
print("Hello")
print("Rudra")
```

Output:

```text
Hello
Rudra
```

Multiple values can also be passed to `print()`:

```python
print("Rudra", "Python")
```

Output:

```text
Rudra Python
```

Python displays the arguments on the same line with a space between them by default.

The important learning goal was not simply memorizing `print()`, but practicing **prediction before execution**.

### Mental Model

**Code → Predict → Execute → Compare with actual output**

---

## 10. Programming Through Real-World Problems

Programming concepts were practiced by converting real-world goals into precise computer-like instructions.

### Sandwich Example

A broad goal such as making a sandwich can be broken into specific steps:

- get the bread
- add specific ingredients
- specify quantities
- assemble the sandwich
- cook it
- serve it

This demonstrates **problem decomposition**.

### Student Result Example

A student result problem can be broken into:

- collect marks
- check individual subjects
- calculate total marks
- calculate overall percentage
- apply passing requirements
- produce the final result

This introduced the idea that programs can work with **information and decisions**.

### Vending Machine Example

A vending machine problem can involve:

- selecting a drink
- determining quantity
- calculating the total
- receiving payment
- checking whether payment is sufficient
- handling excess payment
- requesting remaining payment
- cancelling or resetting when appropriate

This demonstrates that programs need to account for different possible situations, not only the normal path.

---

## 11. Debugging Mindset

We practiced identifying problems in instructions and simple code.

A basic debugging process is:

1. Identify what is wrong.
2. Determine why it is wrong.
3. Identify what the instruction depends on.
4. Correct the logic or ordering.
5. Run the program again and observe the result.

Example:

```python
print(name)
name = "Rudra"
```

The program attempts to use `name` before it has been given the required value.

### Mental Model

**Identify → Understand why → Correct → Test**

---

## 12. Problem Decomposition

A large problem can be transformed into smaller, manageable steps.

### General Mental Model

**Goal → Sub-problems → Instructions → Order → Execution → Result**

This is one of the foundational skills of programming.

The same approach can be applied to problems that initially look unrelated.

---

## 13. Dependencies Between Instructions

Some instructions depend on earlier instructions.

For example:

```python
name = "Rudra"
print(name)
```

The value must be available before it can be used.

This gives another useful mental model:

**Create/prepare something → Use it**

Understanding dependencies helps prevent incorrect ordering and makes programs easier to reason about.

---

## 14. Prediction Before Execution

A major practice throughout the learning was to predict what a program would do before running it.

For example:

```python
print("Hello")
print("World")
```

Before executing it, the expected output can be predicted:

```text
Hello
World
```

This develops the ability to mentally trace code instead of relying only on running it.

### Mental Model

**Read code → Build mental execution → Predict result → Run → Verify**

---

## 15. Key Mental Models

### Programming

**Goal → Instructions → Execution → Result**

### Program

**A set of executable instructions for accomplishing a task.**

### Programming Language

**A structured way for humans to express instructions for computers.**

### Python

**A general-purpose programming language used to express those instructions.**

### Problem Solving

**Understand the goal → Break it down → Make instructions precise → Put them in the correct order → Consider possible situations → Test the result**

### Debugging

**Identify → Understand → Correct → Test**

### Code Execution

**Code → Execution → Output**

---

## 16. Concepts Demonstrated

The following concepts and abilities were demonstrated:

- explaining programming in my own words
- explaining what a program is
- explaining why programming languages exist
- explaining Python's role
- distinguishing programming from Python
- breaking unfamiliar real-world problems into smaller steps
- making instructions more precise
- reasoning about instruction order
- understanding dependencies between instructions
- predicting basic Python output before execution
- distinguishing code from output
- identifying basic logical and ordering problems
- modifying simple Python code to satisfy a requirement
- developing a basic debugging mindset
- reasoning about possible situations in a program
- thinking about programs as a sequence of precise instructions

---

## 17. Core Takeaway

Programming is not primarily about memorizing syntax.

The foundation is:

**Understand the problem → Break it down → Define precise instructions → Put them in the correct order → Execute → Observe the result → Debug when necessary**

Python is the language used to express those instructions.
