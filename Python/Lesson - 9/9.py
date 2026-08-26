# Python Mastery — Lesson 9
# Sets & Set Operations — All Practice Code


# ============================================================
# 1. Set Mental Model — Unique Elements
# ============================================================

numbers = {10, 20, 10, 30, 20, 10}

print(numbers)


# ============================================================
# 2. Set Membership
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

print("Rudra" in students)
print("Virat" in students)


# ============================================================
# 3. Creating a Set
# ============================================================

numbers = {1, 2, 3}

print(numbers)


# ============================================================
# 4. Empty Set vs Empty Dictionary
# ============================================================

empty_dictionary = {}
empty_set = set()

print(type(empty_dictionary))
print(type(empty_set))


# ============================================================
# 5. Duplicate Values in a Set
# ============================================================

numbers = {10, 20, 10, 30, 20, 10}

print(numbers)


# ============================================================
# 6. Set Does Not Support Numeric Indexing
# ============================================================

numbers = {10, 20, 30}

# This raises TypeError:
# print(numbers[0])


# ============================================================
# 7. Iterating Through a Set
# ============================================================

numbers = {10, 20, 30}

for number in numbers:
    print(number)


# ============================================================
# 8. Adding an Element
# ============================================================

students = {"Rudra", "Aarav"}

students.add("Kabir")

print(students)


# ============================================================
# 9. Adding an Existing Element
# ============================================================

students = {"Rudra", "Aarav"}

students.add("Rudra")

print(students)


# ============================================================
# 10. Set State Changes with add()
# ============================================================

numbers = {10, 20}

numbers.add(30)
print(numbers)

numbers.add(10)
print(numbers)

numbers.add(40)
print(numbers)


# ============================================================
# 11. Removing an Existing Element with remove()
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

students.remove("Aarav")

print(students)


# ============================================================
# 12. remove() with an Absent Element — Key Error Behavior
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

# This raises KeyError:
# students.remove("Virat")


# ============================================================
# 13. discard() with an Existing Element
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

students.discard("Aarav")

print(students)


# ============================================================
# 14. discard() with an Absent Element
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

students.discard("Virat")

print(students)


# ============================================================
# 15. Union
# Everything from Both Sets
# ============================================================

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A.union(B))


# ============================================================
# 16. Intersection
# Common Elements from Both Sets
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A & B)
print(A.intersection(B))


# ============================================================
# 17. Difference
# Elements in A but Not in B
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
print(A.difference(B))


# ============================================================
# 18. Difference — Direction Matters
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)
print(B - A)


# ============================================================
# 19. Symmetric Difference
# Elements in Either Set but Not Both
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A ^ B)
print(A.symmetric_difference(B))


# ============================================================
# 20. Executing All Four Set Operations
# ============================================================

A = {10, 20, 30}
B = {30, 40, 50}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)


# ============================================================
# 21. List → Set
# Remove Duplicate Values
# ============================================================

students = ["Rudra", "Aarav", "Rudra", "Kabir", "Aarav"]

unique_students = set(students)

print(unique_students)


# ============================================================
# 22. List → Set → List
# Duplicate-Free List
# ============================================================

students = ["Rudra", "Aarav", "Rudra", "Kabir", "Aarav", "Virat"]

unique_students = list(set(students))

print(unique_students)


# ============================================================
# 23. Count Unique Students
# ============================================================

students = ["Rudra", "Aarav", "Kabir", "Rudra", "Virat", "Kabir"]

unique_students = set(students)

count = len(unique_students)

print(count)


# ============================================================
# 24. Find Common Students Between Two Lists
# ============================================================

morning_batch = ["Rudra", "Aarav", "Kabir", "Virat"]
evening_batch = ["Kabir", "Virat", "Messi", "Neymar"]

morning = set(morning_batch)
evening = set(evening_batch)

common_students = morning & evening

print(common_students)


# ============================================================
# 25. Set + List Integration
# ============================================================

students = ["Rudra", "Aarav", "Rudra", "Kabir", "Aarav", "Virat"]

unique_students = set(students)

print(unique_students)


# ============================================================
# 26. Debugging — remove() vs discard()
# ============================================================

students = {"Rudra", "Aarav", "Kabir"}

# The requirement is to remove Messi only if Messi exists.
# remove() would raise an error if Messi is absent.
# discard() safely handles the absent case.

students.discard("Messi")

print(students)


# ============================================================
# 27. Unfamiliar Challenge
# Count Students Appearing More Than Once
# ============================================================

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


# ============================================================
# 28. Data-Structure Selection
# ============================================================

numbers_list = [1, 2, 3, 4]

numbers_tuple = (1, 2, 3, 4)

numbers_set = {1, 2, 3, 4}

numbers_dictionary = {
    "a": 1,
    "b": 2
}

print(numbers_list)
print(numbers_tuple)
print(numbers_set)
print(numbers_dictionary)