# Python Mastery — Lesson 8
# Dictionaries — All Practice Code


# ============================================================
# 1. Dictionary Mental Model
# ============================================================

student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT",
    "marks": 85
}

print(student["course"])


# ============================================================
# 2. Empty Dictionary
# ============================================================

student = {}

print(student)


# ============================================================
# 3. Adding a New Entry
# ============================================================

student = {}

student["name"] = "Rudra"

print(student)


# ============================================================
# 4. Adding Another New Key
# ============================================================

student = {
    "name": "Rudra"
}

student["age"] = 17

print(student)


# ============================================================
# 5. Modifying an Existing Key's Value
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

student["age"] = 18

print(student)


# ============================================================
# 6. Accessing a Missing Key — KeyError
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

# This raises KeyError:
# print(student["marks"])


# ============================================================
# 7. Dictionary Membership — Checks Keys
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

print("age" in student)
print("Rudra" in student)
print(17 in student)


# ============================================================
# 8. Dictionary State Changes + Membership
# ============================================================

student = {}

student["name"] = "Rudra"
student["age"] = 17
student["age"] = 18

print(student)
print("name" in student)
print(17 in student)


# ============================================================
# 9. Removing an Entry with del
# ============================================================

student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT"
}

del student["age"]

print(student)
print("age" in student)


# ============================================================
# 10. del with a Missing Key — KeyError
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

# This raises KeyError:
# del student["marks"]


# ============================================================
# 11. pop() — Remove Entry and Get Its Value
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

removed_age = student.pop("age")

print(removed_age)
print(student)


# ============================================================
# 12. pop() Without Assigning the Returned Value
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

student.pop("age")

print(student)


# ============================================================
# 13. pop() with a Missing Key — KeyError
# ============================================================

student = {
    "name": "Rudra"
}

# This raises KeyError:
# removed = student.pop("age")


# ============================================================
# 14. Dictionary Keys
# ============================================================

student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT"
}

print(student.keys())


# ============================================================
# 15. Dictionary Values
# ============================================================

print(student.values())


# ============================================================
# 16. Dictionary Items
# ============================================================

print(student.items())


# ============================================================
# 17. Direct Dictionary Iteration — Keys
# ============================================================

student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT"
}

for key in student:
    print(key)


# ============================================================
# 18. Iterating Through Key-Value Pairs
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

for key, value in student.items():
    print(key, value)


# ============================================================
# 19. Iterating Through Only Values
# ============================================================

student = {
    "name": "Rudra",
    "age": 17,
    "course": "IT"
}

for value in student.values():
    print(value)


# ============================================================
# 20. Iterating Through Only Keys
# ============================================================

students = {
    "Rudra": 85,
    "Meghshyam": 92,
    "Aarav": 78
}

for key in students:
    print(key)


# ============================================================
# 21. Updating a Dictionary Value
# ============================================================

marks = {
    "Rudra": 75,
    "Meghshyam": 82,
    "Aarav": 68
}

marks["Aarav"] = 78

print(marks)


# ============================================================
# 22. Updating a Value Using Its Current Value
# ============================================================

marks = {
    "Rudra": 70,
    "Aarav": 85,
    "Meghshyam": 90
}

marks["Aarav"] = marks["Aarav"] + 10

print(marks)


# ============================================================
# 23. Updating Every Value Using Dictionary Keys
# ============================================================

scores = {
    "Rudra": 70,
    "Aarav": 85,
    "Meghshyam": 90
}

for student in scores:
    scores[student] = scores[student] + 5

print(scores)


# ============================================================
# 24. Updating Every Value Using items()
# ============================================================

scores = {
    "Rudra": 70,
    "Aarav": 85,
    "Meghshyam": 90
}

for student, score in scores.items():
    scores[student] = score + 5

print(scores)


# ============================================================
# 25. get() — Missing Key Returns None
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

print(student.get("marks"))


# ============================================================
# 26. get() — Default Value
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

print(student.get("marks", 0))


# ============================================================
# 27. get() — Existing Key Ignores Default
# ============================================================

print(student.get("age", 0))


# ============================================================
# 28. get() Does Not Modify the Dictionary
# ============================================================

student = {
    "name": "Rudra",
    "age": 17
}

result = student.get("marks", 0)

print(result)
print(student)


# ============================================================
# 29. Nested Dictionary
# ============================================================

student = {
    "name": "Rudra",
    "details": {
        "age": 17,
        "course": "IT"
    }
}

print(student["details"]["course"])


# ============================================================
# 30. Nested Access When the First Value Is Not a Dictionary
# ============================================================

student = {
    "name": "Rudra",
    "details": 17
}

# This raises TypeError:
# print(student["details"]["course"])


# ============================================================
# 31. Dictionary → Dictionary → List → Index
# ============================================================

student = {
    "details": {
        "age": 17,
        "skills": ["Python", "HTML"]
    }
}

print(student["details"]["skills"][0])


# ============================================================
# 32. Dictionaries + Conditions
# Print Students Scoring 80 or More
# ============================================================

students = {
    "Rudra": 85,
    "Aarav": 62,
    "Meghshyam": 91
}

for name, score in students.items():
    if score >= 80:
        print(name)


# ============================================================
# 33. Dictionaries + Accumulator
# Calculate Total Score
# ============================================================

students = {
    "Rudra": 85,
    "Aarav": 62,
    "Meghshyam": 91
}

total_score = 0

for score in students.values():
    total_score += score

print(total_score)


# ============================================================
# 34. Dictionaries + Condition + Counter
# Count Students Scoring 80 or More
# ============================================================

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


# ============================================================
# 35. Dictionaries + Functions
# Calculate Average Score
# ============================================================

def find_avg(scores):
    total_score = 0
    count_score = 0

    for score in scores.values():
        total_score += score
        count_score += 1

    return total_score / count_score


print(find_avg({
    "Rudra": 85,
    "Aarav": 72,
    "Meghshyam": 91
}))


# ============================================================
# 36. Cumulative Challenge
# Return Students Scoring 80 or More
# ============================================================

scores = {
    "Rudra": 85,
    "Aarav": 72,
    "Meghshyam": 91,
    "Kabir": 64,
    "Neel": 88
}

def get_top_students(scores):
    final_list = []

    for name, score in scores.items():
        if score >= 80:
            final_list += [name]

    return final_list


print(get_top_students(scores))


# ============================================================
# 37. Alternative: append() Version
# Same result as += [name]
# ============================================================

def get_top_students(scores):
    final_list = []

    for name, score in scores.items():
        if score >= 80:
            final_list.append(name)

    return final_list


print(get_top_students(scores))


# ============================================================
# 38. Final Unfamiliar Challenge
# Return Out-of-Stock Products
# ============================================================

inventory = {
    "laptop": 5,
    "mouse": 12,
    "keyboard": 3,
    "headphones": 0
}

def check_inventory(inventory):
    out_of_stock = []

    for product_name, quantity in inventory.items():
        if quantity == 0:
            out_of_stock += [product_name]

    return out_of_stock


print("Current Out of Stock Products:", check_inventory(inventory))


# ============================================================
# 39. Final Lesson Check
# Safe City Retrieval with get()
# ============================================================

user = {
    "name": "Rudra",
    "age": 17,
    "city": "Nashik"
}

def show_city(user):
    users_city = user.get("city", "Unknown")

    return users_city


print(show_city(user))

