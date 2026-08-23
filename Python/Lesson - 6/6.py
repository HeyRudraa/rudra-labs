# ============================================
# PYTHON MASTERY — LESSON 6
# Lists
# ============================================


# 1. List Iteration

marks = [72, 85, 91]

for mark in marks:
    print(mark + 5)



# 2. List + Conditions

marks = [72, 85, 91]

for mark in marks:
    if mark >= 80:
        print(mark)



# 3. Loop Variable vs List

marks = [72, 85, 91]

for mark in marks:
    mark = mark + 5

print(marks)



# 4. Modifying List Elements

marks = [72, 85, 91]

for i in range(len(marks)):
    marks[i] = marks[i] + 5

print(marks)



# 5. List Indexing

marks = [72, 85, 91, 68]

print(marks[1])
print(marks[3])
print(marks[-1])



# 6. Index Modification

numbers = [10, 20, 30, 40, 50]

numbers[1] = 99
numbers[-1] = 5
numbers[2] = numbers[0] + numbers[1]

print(numbers)



# 7. Modify Every Element

numbers = [12, 7, 25, 4, 18]

for number in range(len(numbers)):
    numbers[number] = numbers[number] + 10

numbers[-1] = 100

print(numbers)



# 8. append()

numbers = [10, 20, 30]

result = numbers.append(40)

print(numbers)
print(result)



# 9. insert()

numbers = [10, 20, 30]

numbers.insert(1, 99)

print(numbers)



# 10. insert() vs Index Assignment

numbers = [10, 20, 30]

numbers.insert(1, 99)

print(numbers)

numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)



# 11. remove()

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)



# 12. pop() with Index

numbers = [10, 20, 30, 40]

x = numbers.pop(1)

print(numbers)
print(x)



# 13. pop() Without Index

numbers = [10, 20, 30]

x = numbers.pop()

print(numbers)
print(x)



# 14. len()

numbers = [10, 20, 30, 40]

print(len(numbers))



# 15. len() After append() and pop()

numbers = [10, 20, 30]

numbers.append(40)
numbers.pop()

print(len(numbers))



# 16. Different Values in a List

items = [10, "", None, 40]

print(len(items))



# 17. Membership with in

names = ["Rudra", "Messi", "Argentina"]

print("Messi" in names)
print("Brazil" in names)



# 18. Membership with not in

names = ["Rudra", "Messi", "Argentina"]

print("Ronaldo" not in names)
print("Messi" not in names)



# 19. Membership + if/else

marks = [45, 72, 88, 39, 91]

if 50 in marks:
    print("Found")
else:
    print("Not Found")



# 20. Basic Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[2:5])



# 21. Slicing Beyond Available Index

numbers = [10, 20, 30]

print(numbers[1:10])



# 22. Cumulative List Challenge

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
numbers[1] = 25
numbers.pop(3)

print(numbers)
print(numbers[1:4])
print(40 in numbers)
