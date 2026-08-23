# ============================================
# PYTHON MASTERY — LESSON 5
# Functions & Program Decomposition
# ============================================


# 1. Basic Function
def greet():
    print("Hello")


greet()


# 2. Function with Parameter
def greet_name(name):
    print("Hello", name)


greet_name("Rudra")
greet_name("Messi")


# 3. Multiple Parameters
def calculate(a, b):
    result = a + b
    print(result)


calculate(5, 3)
calculate(10, 2)


# 4. return
def add(a, b):
    result = a + b
    return result


x = add(4, 6)
print(x)


# 5. print() vs return
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


x = add_print(2, 3)
y = add_return(2, 3)

print("x =", x)
print("y =", y)


# 6. return ends function execution
def test():
    print("A")
    return 10
    print("B")


x = test()
print(x)


# 7. Conditional return
def check(number):
    if number > 10:
        return "Big"

    return "Small"


print(check(15))
print(check(7))


# 8. is_even()
def is_even(num):
    if num % 2 == 0:
        return "Even"

    return "Odd"


print(is_even(8))
print(is_even(7))


# 9. max_of_three()
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(max_of_three(10, 25, 7))
print(max_of_three(50, 20, 80))
print(max_of_three(5, 5, 3))

# Equality cases
print(max_of_three(5, 3, 5))
print(max_of_three(5, 5, 5))


# 10. check_result()
def check_result(marks):
    if marks >= 40:
        return "Pass"

    return "Fail"


print(check_result(40))
print(check_result(20))
print(check_result(90))


# 11. Student Result
def check_student_result(marks1, marks2, marks3):
    avg_marks = (marks1 + marks2 + marks3) / 3

    if avg_marks >= 40:
        return "Pass"

    return "Fail"


print(check_student_result(40, 40, 40))
print(check_student_result(20, 60, 24))
print(check_student_result(90, 89, 96))


# 12. ticket_price()
# Extended version with age validation/edge-case thinking
def ticket_price(age):
    if age < 5:
        return "Free"

    elif age < 18:
        return "100"

    elif age < 110:
        return "200"

    else:
        return "Invalid Age"


ticket_price(3)
ticket_price(10)
ticket_price(17)
ticket_price(25)
ticket_price(30)


# 13. calculate_bill()
def calculate_bill(units):
    if units <= 100:
        return "Low Usage"

    elif units <= 300:
        return "Medium Usage"

    else:
        return "High Usage"


print(calculate_bill(100))
print(calculate_bill(101))
print(calculate_bill(300))
print(calculate_bill(301))


# 14. Scope
x = 10


def scope_test():
    x = 20
    print(x)


scope_test()
print(x)


# 15. Parameter is local
x = 100


def change(x):
    x = x + 50
    return x


result = change(10)

print("result =", result)
print("x =", x)


# 16. Reading an outer variable
x = 10


def read_outer():
    print(x)


read_outer()


# 17. Nested Function
def outer():
    x = 50

    def inner():
        print(x)

    inner()


outer()


# 18. Function calling another function
def greet_function():
    print("Hello")


def start():
    greet_function()


start()