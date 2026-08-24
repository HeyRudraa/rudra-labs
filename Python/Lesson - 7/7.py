# 🐍 Python Mastery — Lesson 7
# Tuples & Immutable Collections



# ============================================================
# 1. Tuple Creation
# ============================================================

numbers = (10, 20, 30)
single_item_tuple = (10,)
empty_tuple = ()

print("Tuple:", numbers)
print("Single-item tuple:", single_item_tuple)
print("Empty tuple:", empty_tuple)

# Important syntax:
# (10)  -> int
# (10,) -> tuple


# ============================================================
# 2. Tuple Indexing and Slicing
# ============================================================

data = (50, 100, 150, 200)

print("\nIndex 1:", data[1])
print("Last value:", data[-1])
print("Slice:", data[1:3])

# Indexing reads a value.
# Index assignment would try to modify the tuple and is not allowed:
#
# data[1] = 999  # TypeError


# ============================================================
# 3. Tuple Iteration and Accumulator
# ============================================================

scores = (5, 10, 15, 20)

total = 0

for score in scores:
    total += score

print("\nScores:", scores)
print("Total:", total)


# ============================================================
# 4. Tuple Operations
# ============================================================

numbers = (10, 20, 30, 20, 40)

print("\nLength:", len(numbers))
print("20 exists:", 20 in numbers)
print("99 exists:", 99 in numbers)
print("Count of 20:", numbers.count(20))
print("First index of 20:", numbers.index(20))


# ============================================================
# 5. Tuple Reassignment
# ============================================================

numbers = (10, 20, 30)

# This does NOT modify the original tuple.
# A new tuple is created and assigned to numbers.
numbers = numbers + (40,)

print("\nAfter reassignment:", numbers)


# ============================================================
# 6. Tuple + Mutable Object
# ============================================================

data = ([1, 2], 3)

# The tuple element itself is not replaced.
# The list stored inside the tuple is modified.
data[0].append(4)

print("\nTuple containing mutable object:", data)


# ============================================================
# 7. Tuples as Function Return Values
# ============================================================

def get_student():
    return ("Rudra", 85)


student = get_student()

print("\nStudent name:", student[0])
print("Student score:", student[1])


# ============================================================
# 8. Independent Challenge — Analyze Scores
# ============================================================

def analyze_scores(scores):
    total_score = 0

    for score in scores:
        total_score += score

    return (len(scores), total_score, scores.index(80))


print("\nScore analysis:")
print(analyze_scores((50, 80, 80, 90, 70)))


# ============================================================
# 9. Final Integrated Challenge
# ============================================================

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


print("\nFinal number analysis:")
print(analyze_numbers((12, 7, 12, 20, 5, 7, 30)))


# ============================================================
# 10. State Tracing Example
# ============================================================

data = (10, 20, 30)

result = data[1:]
data = data + (40,)

print("\nSliced result:", result)
print("Reassigned data:", data)

