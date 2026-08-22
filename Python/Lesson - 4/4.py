
# --------------------------------------------
# 1. Finding numbers divisible by both 3 and 5
# --------------------------------------------

for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print(number)


# --------------------------------------------
# 2. Skip even numbers and stop at 15
# --------------------------------------------

for number in range(1, 21):
    if number % 2 == 0:
        continue

    print(number)

    if number == 15:
        break


# --------------------------------------------
# 3. First number divisible by both 4 and 7
# --------------------------------------------

for number in range(1, 101):
    if number % 7 == 0 and number % 4 == 0:
        print(number)
        break


# --------------------------------------------
# 4. Sum of even numbers from 1 to 20
# --------------------------------------------

even_sum = 0

for number in range(1, 21):
    if number % 2 == 0:
        even_sum += number

print("The total sum of even number between 1 to 20 is:", even_sum)


# --------------------------------------------
# 5. Count numbers divisible by both 3 and 5
# --------------------------------------------

count = 0

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        count += 1

print(count)


# --------------------------------------------
# 6. First number divisible by 4 but not 6
# --------------------------------------------

for number in range(1, 51):
    if number % 4 == 0 and number % 6 != 0:
        print(number)
        break


# --------------------------------------------
# 7. Count first 4 numbers divisible by 3
# --------------------------------------------

count = 0

for number in range(1, 101):
    if number % 3 == 0:
        print(number)
        count += 1

        if count == 4:
            break


# --------------------------------------------
# 8. Sum of first 5 numbers divisible by
#    either 3 or 5, but not both
# --------------------------------------------

count = 0
total = 0

for number in range(1, 101):

    if count == 5:
        break

    if number % 3 == 0 and number % 5 != 0:
        count += 1
        total += number

    elif number % 3 != 0 and number % 5 == 0:
        count += 1
        total += number

print("The sum is:", total)


# --------------------------------------------
# 9. Final Lesson 4 Mastery Challenge
#    First 3 numbers divisible by 4 but
#    NOT divisible by 6, then sum them
# --------------------------------------------

count = 0
total = 0

for number in range(1, 101):

    if count == 3:
        break

    if number % 4 == 0 and number % 6 != 0:
        count += 1
        total += number

print("The sum is:", total)