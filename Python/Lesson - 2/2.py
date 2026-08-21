# ============================================================
# LESSON 2 — VALUES, VARIABLES, EXPRESSIONS & OPERATORS
# ============================================================


# ============================================================
# 1. VARIABLES AND BASIC VALUES
# ============================================================

student_name = "Rudra"
student_age = 17
student_marks = 85

print(student_name)
print(student_age)
print(student_marks)


# ============================================================
# 2. PRINTING VARIABLES WITH FORMATTING
# ============================================================

print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)


# ============================================================
# 3. PRINT() — sep, end, AND NEWLINES
# ============================================================

print("Name", student_name, sep=": ")
print("Age", student_age, sep=": ")
print("Marks:", end=" ")
print(student_marks)


# ============================================================
# 4. STRINGS AND QUOTE TYPES
# ============================================================

message_1 = 'Rudra said "Python" is fun'
message_2 = "Rudra said 'Python' is fun"

print(message_1)
print(message_2)


# ============================================================
# 5. ESCAPING QUOTES INSIDE STRINGS
# ============================================================

message_3 = "Rudra said, \"Python's variables are powerful!\" and then printed: 'Hello, World!'"

print(message_3)


# ============================================================
# 6. VARIABLES AND REASSIGNMENT
# ============================================================

name = "Rudra"
age = 17

print(name)
print(age)

name = "Messi"
age = 39

print(name)
print(age)


# ============================================================
# 7. ASSIGNING ONE VARIABLE FROM ANOTHER
# ============================================================

x = 10
y = x

print(x)
print(y)

x = 20

print(x)
print(y)


# ============================================================
# 8. ASSIGNMENT AND REASSIGNMENT WITH DIFFERENT VALUES
# ============================================================

a = 5
b = a

a = 10
b = a

print(a)
print(b)


# ============================================================
# 9. EXPRESSIONS AND BASIC ARITHMETIC
# ============================================================

a = 10
b = 5

result = a + b

print(result)


# ============================================================
# 10. OPERATORS AND OPERANDS
# ============================================================

x = 10
y = x * 3 + 2

print(y)


# ============================================================
# 11. OPERATOR PRECEDENCE
# ============================================================

a = 20
b = 5

result = a - b * 2

print(result)


# ============================================================
# 12. MULTIPLE OPERATORS WITH THE SAME PRECEDENCE
# ============================================================

a = 10
b = 3
c = 2

result = a + b * c - 4

print(result)


# ============================================================
# 13. PARENTHESES AND EXPRESSION GROUPING
# ============================================================

a = 10
b = 2
c = 3

result = (a + b) * c - 4

print(result)


# ============================================================
# 14. EXPRESSIONS WITHOUT VARIABLES
# ============================================================

a = 10 + 5
b = "Hello" + " Rudra"

print(a)
print(b)


# ============================================================
# 15. STRING CONCATENATION
# ============================================================

first_name = "Rudra"
greeting = "Hello " + first_name

print(greeting)


# ============================================================
# 16. TYPE DIFFERENCES IN EXPRESSIONS
# ============================================================

age = 17
text_age = "17"

print(age + 1)
print(text_age + "1")


# ============================================================
# 17. TYPE ERROR FROM INCOMPATIBLE OPERANDS
# ============================================================

# The following expression would raise TypeError:
#
# result = 10 + "5"
#
# int + str cannot be used for normal addition.


# ============================================================
# 18. TYPE CONVERSION WITH str()
# ============================================================

age = 17
text_age = str(age)

print(text_age)
print(age)


# ============================================================
# 19. TYPE CONVERSION WITH int()
# ============================================================

quantity = "3"

quantity_as_int = int(quantity)

print(quantity_as_int)


# ============================================================
# 20. CHECKING TYPES WITH type()
# ============================================================

a = 25
b = "25"

print(type(a))
print(type(b))


# ============================================================
# 21. type() WITH EXPRESSIONS
# ============================================================

print(type(10 + 5))
print(type("Hello" + " Rudra"))
print(type(10 / 2))


# ============================================================
# 22. STORING THE RESULT OF type()
# ============================================================

a = 10
b = "10"

x = type(a)
y = type(b)

print(x)
print(y)


# ============================================================
# 23. DIVISION, FLOOR DIVISION, AND MODULO
# ============================================================

a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)


# ============================================================
# 24. CHECKING THE TYPES OF ARITHMETIC RESULTS
# ============================================================

a = 17
b = 5

print(a / b)
print(type(a / b))

print(a // b)
print(type(a // b))

print(a % b)
print(type(a % b))


# ============================================================
# 25. MODULO FOR REMAINDERS
# ============================================================

a = 24
b = 7

print(a % b)
print(b % 2)
print(a // b)


# ============================================================
# 26. REAL-WORLD USE OF // AND %
# ============================================================

total = 1250
people = 4

share = total // people
remainder = total % people

print(share)
print(remainder)


# ============================================================
# 27. CONVERTING SECONDS INTO MINUTES AND REMAINING SECONDS
# ============================================================

seconds = 367

minutes = seconds // 60
remaining_seconds = seconds % 60

print(minutes)
print(remaining_seconds)


# ============================================================
# 28. STRING REPETITION WITH *
# ============================================================

print("Ha" * 3)
print(3 * "Ha")


# ============================================================
# 29. STRING CONCATENATION VS INTEGER ADDITION
# ============================================================

print("Ha" + "!")
print(10 + 5)


# ============================================================
# 30. EVALUATION OF EXPRESSIONS BEFORE ASSIGNMENT
# ============================================================

x = 10
y = x + 5

x = 100

print(x)
print(y)


# ============================================================
# 31. ASSIGNMENT USING THE CURRENT VALUE OF A VARIABLE
# ============================================================

score = 10

score = score + 5
score = score * 2

print(score)


# ============================================================
# 32. AUGMENTED ASSIGNMENT OPERATORS
# ============================================================

points = 10

points += 5
points *= 2
points -= 4

print(points)


# ============================================================
# 33. PRODUCT TOTAL CALCULATION
# ============================================================

price = 500
quantity = 2
discount = 100

total = price * quantity - discount

print(total)


# ============================================================
# 34. TYPE CONVERSION INSIDE AN EXPRESSION
# ============================================================

price = 500
quantity = "3"

total = price * int(quantity)

print(total)


# ============================================================
# 35. SHOPPING BILL — INDEPENDENT PRACTICAL TASK
# ============================================================

item_price = 250
item_quantity = 3
discount = "50"

int_discount = int(discount)

sub_total = item_price * item_quantity
total = sub_total - int_discount

print("Item Price:", item_price)
print("Quantity:", item_quantity)
print("Discount:", int_discount)
print("Subtotal:", sub_total)
print("Final Total:", total)


# ============================================================
# 36. STUDENT MARKS — FINAL LESSON 2 PRACTICAL
# ============================================================

sub_math = 85
sub_python = 92
sub_science = 78

total_marks = sub_math + sub_python + sub_science
average_marks = total_marks / 3

print("Math:", sub_math)
print("Python:", sub_python)
print("Science:", sub_science)
print("Total:", total_marks)
print("Average:", average_marks)