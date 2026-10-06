#---------------------------------------------------
# 1. Set: checking whether a student exists
# --------------------------------------------------

student_names = {"Rudra", "Aarav", "Megh", "Rahul", "Sahil"}

search_name = input("Enter a student name: ")

if search_name in student_names:
    print("Student found")
else:
    print("Student not found")


# --------------------------------------------------
# 2. Dictionary: student name -> marks
# --------------------------------------------------

student_marks = {
    "Rudra": 85,
    "Aarav": 91,
    "Megh": 78,
    "Rahul": 66,
    "Sahil": 88
}

search_name = input("Enter a student name to get marks: ")

if search_name in student_marks:
    print("Marks:", student_marks[search_name])
else:
    print("Student not found")


# --------------------------------------------------
# 3. Linear Search
# --------------------------------------------------

numbers = [4, 8, 2, 9, 1, 7]

search_number = int(input("Enter a number to search: "))
found = False

for number in numbers:
    if number == search_number:
        print("Number found")
        found = True
        break

if not found:
    print("Number not found")


# --------------------------------------------------
# 4. Linear Search with an empty-list edge case
# --------------------------------------------------

numbers = []

search_number = int(input("Enter a number to search in the list: "))

if not numbers:
    print("List is empty")
else:
    found = False

    for number in numbers:
        if number == search_number:
            print("Number found")
            found = True
            break

    if not found:
        print("Number not found")


# --------------------------------------------------
# 5. Binary Search
# --------------------------------------------------
# Binary search works on sorted data.
# The search range is repeatedly reduced by half.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_number = int(input("Enter a number to binary search: "))

left = 0
right = len(numbers) - 1
found = False

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == search_number:
        print("Number found")
        found = True
        break

    if search_number < numbers[middle]:
        right = middle - 1
    else:
        left = middle + 1

if not found:
    print("Number not found")
