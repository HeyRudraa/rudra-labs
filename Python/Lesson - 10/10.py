##############################################################################
# FINAL LESSON — ASSESSMENT / TRACE / DEBUGGING CODE
##############################################################################

# -----------------------------
# 1. Variables and state
# -----------------------------

x = 10
y = x + 5
x = 20

print(y)


# -----------------------------
# 2. Conditions
# -----------------------------

x = 8

if x > 5 and x < 10:
    print("A")
elif x == 8:
    print("B")
else:
    print("C")


# -----------------------------
# 3. Loops and continue
# -----------------------------

total = 0

for i in range(1, 5):
    if i == 3:
        continue
    total += i

print(total)


# -----------------------------
# 4. Functions and local state
# -----------------------------

def calculate(x):
    x = x * 2
    return x


a = 5
b = calculate(a)

print(a)
print(b)


# -----------------------------
# 5. Lists and pop
# -----------------------------

numbers = [10, 20, 30, 40]

x = numbers.pop(1)
numbers.append(50)

print(x)
print(numbers)


# -----------------------------
# 6. Dictionaries
# -----------------------------

student = {
    "name": "Rudra",
    "marks": 80
}

student["marks"] += 5
student["grade"] = "A"

print(student)


# -----------------------------
# 7. Tuples and reassignment
# -----------------------------

data = (10, 20, 30)

data = data + (40,)

print(data)


# -----------------------------
# 8. Sets
# -----------------------------

numbers = [1, 2, 2, 3, 3, 3, 4]

unique = set(numbers)

print(unique)
print(len(unique))


# -----------------------------
# 9. Function + list + condition
# -----------------------------

def process(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n * 2)

    return result


data = [1, 2, 3, 4, 5]
output = process(data)

print(data)
print(output)


# -----------------------------
# 10. Loop + state + list mutation
# -----------------------------

numbers = [2, 5, 8]

total = 0

for number in numbers:
    if number > 4:
        total += number
    else:
        total -= number

numbers.append(total)

print(total)
print(numbers)


# -----------------------------
# 11. continue + membership
# -----------------------------

values = [3, 6, 3]

result = []

for value in values:
    if value in result:
        continue

    result.append(value)

print(result)


# -----------------------------
# 12. Function mutating a list
# -----------------------------

def update(values):
    values.append(10)
    return len(values)


numbers = [1, 2, 3]

x = update(numbers)

numbers.append(x)

print(x)
print(numbers)


# -----------------------------
# 13. Dictionary state updates
# -----------------------------

scores = {
    "A": 10,
    "B": 5,
    "C": 8
}

for name in scores:
    if scores[name] >= 8:
        scores[name] += 2
    else:
        scores[name] += 1

print(scores)


# -----------------------------
# 14. Nested conditions + set/list result
# -----------------------------

def process(data):
    result = []

    for item in data:
        if item in result:
            continue

        if item % 2 == 0:
            result.append(item * 2)
        else:
            result.append(item)

    return result


numbers = [2, 3, 2, 4, 3]

output = process(numbers)

print(numbers)
print(output)


# -----------------------------
# 15. Debugging: accumulator
# Requirement: sum all even numbers.
# Bug: -= should be +=.
# -----------------------------

numbers = [1, 2, 3, 4, 5, 6]

total = 0

for number in numbers:
    if number % 2 == 0:
        total -= number

print(total)


# -----------------------------
# 16. Debugging: range boundary
# Requirement: print 1 through 5.
# Bug: stop value is excluded.
# -----------------------------

for i in range(1, 5):
    print(i)


# -----------------------------
# 17. Debugging: print vs return
# Requirement: return the total to the caller.
# Bug: print(total) does not return it.
# -----------------------------

def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    print(total)


numbers = [10, 20, 30]

result = calculate_total(numbers)

print(result)


# -----------------------------
# 18. Debugging: list + int
# Requirement: add one number to a list.
# Bug: list + int is invalid.
# Correct form: result + [number]
# -----------------------------

numbers = [2, 7, 4, 9, 3, 8]

result = []

for number in numbers:
    if number > 5:
        result = result + [number]

print(result)


# -----------------------------
# 19. Debugging: membership condition
# Requirement: collect unique values.
# Bug: checking "in" instead of "not in".
# -----------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for number in numbers:
    if number in unique:
        unique.append(number)

print(len(unique))


##############################################################################
# FINAL LESSON — INTEGRATED PROBLEM 1: STUDENT RESULTS
##############################################################################

# Final Lesson — Integrated Problem
# Student Results

students = [
    ("Rudra", 82),
    ("Aman", 45),
    ("Rahul", 67),
    ("Priya", 91),
    ("Neha", 38)
]


def average_marks(students):
    total_marks = 0

    for student in students:
        total_marks += student[1]

    return total_marks / len(students)


average = average_marks(students)
passed_students = []
failed_students = []
unique_marks = set()

for name, marks in students:
    if marks >= 50:
        passed_students.append(name)
    else:
        failed_students.append(name)

    unique_marks.add(marks)

print(passed_students)
print(failed_students)
print(average)
print(unique_marks)


##############################################################################
# FINAL LESSON — INTEGRATED PROBLEM 2: INVENTORY TRACKER
##############################################################################

# Final Lesson — Integrated Problem
# Inventory Tracker

def is_available(inventory, item):
    return item in inventory


inventory = {
    "laptop": 5,
    "mouse": 12,
    "keyboard": 7,
    "headphones": 3
}

good_stock = []
total_stock = 0
stock_quantity = set()

for product, quantity in inventory.items():
    if quantity > 5:
        good_stock.append(product)

    total_stock += quantity
    stock_quantity.add(quantity)

print(good_stock)
print(total_stock)
print(stock_quantity)

item = input("ENTER PRODUCT TO SEARCH: ")

print(is_available(inventory, item))


##############################################################################
# FINAL LESSON — INTEGRATED PROBLEM 3: TRANSACTION PROCESSOR
##############################################################################

# Final Lesson — Integrated Problem
# Transaction Processor

transactions = [
    ("Rudra", "laptop", 2),
    ("Aman", "mouse", 1),
    ("Rudra", "mouse", 3),
    ("Priya", "laptop", 1),
    ("Aman", "keyboard", 2),
    ("Rudra", "laptop", 1)
]

total_quantity = {}
purchased_laptop = []
all_products = set()
total_products = 0

for name, product, quantity in transactions:
    if name in total_quantity:
        total_quantity[name] += quantity
    else:
        total_quantity[name] = quantity

    if product == "laptop" and name not in purchased_laptop:
        purchased_laptop.append(name)

    all_products.add(product)
    total_products += quantity

print(total_quantity)
print(purchased_laptop)
print(all_products)
print(total_products)


##############################################################################
# FINAL CAPSTONE — STUDENT RECORD SYSTEM
##############################################################################

# Module 1 — Final Capstone
# Student Record System

def latest_records(records):
    latest = {}

    for name, marks in records:
        latest[name] = marks

    return latest


students = [
    ("Rudra", 82),
    ("Aman", 45),
    ("Rahul", 67),
    ("Priya", 91),
    ("Neha", 38),
    ("Aman", 55)
]

latest_students = latest_records(students)

total_students = len(latest_students)
total_marks = 0
highest_marks = 0
lowest_marks = None
unique_marks = set()
passed_students = []

for name, marks in latest_students.items():
    total_marks += marks

    if marks > highest_marks:
        highest_marks = marks

    if lowest_marks is None or marks < lowest_marks:
        lowest_marks = marks

    unique_marks.add(marks)

    if marks >= 50:
        passed_students.append(name)

average_marks = total_marks / total_students


while True:
    print("""
1. Check student result
2. Check statistics
3. Check unique marks
4. Check passed student list
5. Exit
""")

    choice = int(input("ENTER CHOICE (1-5): "))

    if choice == 1:
        student_name = input("Enter student name: ")

        if student_name in latest_students:
            marks = latest_students[student_name]

            if marks >= 50:
                result = "Pass"
            else:
                result = "Fail"

            print(f"Marks: {marks}")
            print(f"Result: {result}")
        else:
            print("Student doesn't exist.")

    elif choice == 2:
        print(
            f"Total Students: {total_students}\n"
            f"Average Marks: {average_marks}\n"
            f"Highest Marks: {highest_marks}\n"
            f"Lowest Marks: {lowest_marks}"
        )

    elif choice == 3:
        print("Unique Marks:", unique_marks)

    elif choice == 4:
        print("Passed Students:", passed_students)

    elif choice == 5:
        print("\nSuccessfully exited program!")
        break

    else:
        print("Invalid choice! Enter an integer between 1 and 5.")