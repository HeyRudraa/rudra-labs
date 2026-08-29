# Module 2 — Problem Solving
## Lesson 1 — Problem Understanding & Requirement Precision

## 1. Lesson Objective

The objective of Lesson 1 was to establish the first critical problem-solving capability:

> **Unknown Problem → Understand Precisely**

Before implementation, the programmer should understand exactly what problem is being solved and what behavior is actually required.

The lesson focused on learning to:

- identify the actual objective
- extract requirements
- distinguish inputs from outputs
- identify explicit rules and conditions
- recognize ambiguity
- identify unsupported assumptions
- distinguish facts from assumptions
- recognize relevant and irrelevant information
- translate natural-language requirements into precise behavior
- determine when clarification is required before implementation

---

## 2. Core Principle

> **Do not start coding until you understand the problem you are solving.**

A solution can be technically correct Python and still be wrong if it implements an incorrect interpretation of the requirement.

The key habit developed throughout the lesson was:

> **Do not invent missing requirements. Do not ignore provided requirements.**

---

## 3. Concepts Practiced

### 3.1 Identifying the Objective

Given a requirement, first determine what the system is actually supposed to accomplish.

Example:

> “Build a program that tells whether a student passed.”

The objective is to determine whether the student passed.

---

### 3.2 Identifying Inputs and Outputs

Determine:

- what information the program receives
- what information or behavior the program must produce

The input/output must come from the requirement rather than assumptions.

---

### 3.3 Missing Requirements

A requirement may describe the goal without providing enough information to determine exact behavior.

Examples encountered:

- passing criteria not specified
- discount percentage not specified
- delivery-fee rules not specified
- inactivity period not specified
- bonus eligibility criteria not specified

When missing information affects the required behavior, clarification is needed.

---

### 3.4 Facts vs Assumptions

A critical distinction practiced throughout the lesson:

**Fact:**
> The client explicitly states a rule.

**Assumption:**
> The developer chooses a rule because it seems reasonable.

Examples of unsupported assumptions identified:

- assuming a 10% discount
- assuming 30 days means “long time”
- assuming ₹1,000 defines a large order
- assuming 80% lesson completion and 75% attendance for a bonus

A reasonable value is still an assumption if the requirement does not support it.

---

### 3.5 Ambiguous Language

Human language can be understandable to people but still be too vague for deterministic program behavior.

Examples:

- “large order”
- “long time”
- “good attendance”
- “sufficient funds”
- “enough lessons”

The programmer must identify what exact rule gives these concepts operational meaning.

---

### 3.6 Requirement Conflicts

When two requirements produce different outcomes, the programmer should not arbitrarily choose one.

Example:

- Score ≥ 40 → pass
- Score < 50 → fail
- Score 45 → special case

The correct action is to identify the conflict and ask for clarification.

Important distinction:

> **Incomplete requirement ≠ conflicting requirement**

An incomplete requirement is missing information. A conflicting requirement contains rules that cannot all be satisfied consistently without clarification.

---

### 3.7 Boundary Precision

Small wording differences can change behavior.

Example:

> “40 or more”

means:

- 39 → fail
- 40 → pass
- 41 → pass

Therefore:

`>= 40`

is not equivalent to:

`> 40`

Other boundary cases practiced included:

- age 18 or older
- ₹2,000 or more
- withdrawals up to ₹20,000

---

### 3.8 Relevant vs Irrelevant Information

Not every piece of provided information necessarily affects the current problem.

The programmer should ask:

> **Does this information actually affect the behavior we are defining?**

For example, an employee's favorite color does not affect a salary-after-tax calculation unless a requirement explicitly connects it to the behavior.

At the same time, provided information should not be dismissed merely because it initially seems unimportant. Its relevance must be judged against the requirement.

---

### 3.9 Clarification

Good clarification questions are specific.

Weak:

> “Can you explain more?”

Strong:

> “What percentage of attendance qualifies as good attendance?”

> “What order amount should qualify as a large order?”

> “What condition should determine whether the account balance is sufficient for the requested withdrawal?”

The goal is to identify the exact missing rule.

---

## 4. Key Mental Model Developed

The lesson repeatedly practiced this reasoning process:

```text
Requirement
    ↓
What is explicitly known?
    ↓
What information is required?
    ↓
What is missing?
    ↓
What is vague or conflicting?
    ↓
What assumptions are being made?
    ↓
What behavior can be defined with certainty?
    ↓
Do we need clarification?
    ↓
Only then → implementation
```

---

## 5. Major Exercises Practiced

### Student Pass/Fail

Identified:

- required student data
- passing criteria
- expected output
- importance of exact boundary wording

### Product Discount

Identified:

- ₹2,000 threshold
- 20% discount
- no discount below ₹2,000
- final amount as output
- difference between stated rule and invented rules

### Delivery Fee

Identified:

- nearby orders should cost less
- distant orders should cost more
- exact distance ranges and fee rules were missing
- developer's ₹20/₹50 rules were unsupported assumptions

### Account Withdrawal

Identified:

- daily limit of ₹20,000
- sufficient balance requirement
- possible ambiguity around whether a minimum balance must remain
- difference between available balance and a possible bank minimum-balance rule

### Employee Bonus

Identified:

- good performance and sufficient employment duration are required
- exact performance and duration criteria were missing
- developer's 80% and 12-month rules were invented

### Exam Eligibility

Final independent challenge demonstrated that:

- required lesson completion was vague
- good attendance was vague
- 80% and 75% were unsupported assumptions
- edge cases where only one condition is satisfied need clarification
- exact eligibility cannot be implemented confidently without the missing criteria

---

## 6. Demonstrated Capabilities

By the end of the lesson, Rudra demonstrated the ability to independently:

- identify the objective of a requirement
- extract relevant information
- identify missing information
- recognize vague language
- distinguish facts from assumptions
- identify unsupported business rules
- recognize conflicting requirements
- reason about boundary conditions
- distinguish relevant from irrelevant information
- formulate targeted clarification questions
- determine what behavior can be defined with certainty
- determine when implementation should stop until clarification is obtained
- analyze an unfamiliar requirement without relying on a predefined solution pattern

---

## 7. Honest Assessment

### Strengths

Rudra demonstrated strong improvement in:

- identifying missing requirements
- recognizing unsupported assumptions
- handling boundary conditions
- identifying ambiguous business language
- recognizing when clarification is required
- reasoning about edge cases

The strongest evidence came from the final independent analysis, where Rudra correctly identified vague criteria, unsupported developer assumptions, relevant information, clarification needs, and the inability to implement the decision exactly without client clarification.

### Weaknesses to Carry Forward

The main remaining weakness is:

> **Precision under pressure**

At times, Rudra:

- treated a possible question as a necessary clarification
- initially looked for a missing number when the real missing item was a relationship or rule
- sometimes needed to distinguish a reasonable interpretation from an explicitly stated requirement

These are not blockers, but future problem-solving exercises should continue reinforcing them.

---

## 8. Core Lessons to Carry Forward

### Principle 1
> **Do not invent requirements.**

### Principle 2
> **Do not ignore requirements that were actually provided.**

### Principle 3
> **A reasonable assumption is still an assumption unless the requirement supports it.**

### Principle 4
> **Not every missing detail is a blocker.**

Ask whether the missing information actually affects the behavior being defined.

### Principle 5
> **Vague human language must become precise before a program can reliably act on it.**

### Principle 6
> **When requirements conflict, clarify instead of choosing arbitrarily.**

### Principle 7
> **Small wording differences can produce different program behavior.**

---
