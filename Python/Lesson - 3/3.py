# ============================================================
# LESSON 3 — CONDITIONAL LOGIC & CONTROL FLOW
# ============================================================


# ============================================================
# 1. BASIC CONDITION — COMPARISON EXPRESSION
# ============================================================

age = 17

result = age >= 18

print(result)


# ============================================================
# 2. COMPARISON EXPRESSION EVALUATION
# ============================================================

age = 20

result = age >= 18

print(result)


# ============================================================
# 3. BASIC IF STATEMENT
# ============================================================

age = 20

if age >= 18:
    print("Adult")

print("Done")


# ============================================================
# 4. IF CONDITION IS FALSE
# ============================================================

age = 15

if age >= 18:
    print("Adult")

print("Program finished")


# ============================================================
# 5. IF SUITE — MULTIPLE INDENTED STATEMENTS
# ============================================================

score = 75

if score >= 50:
    print("Passed")
    print("Good job")

print("Result checked")


# ============================================================
# 6. BLANK LINE DOES NOT CHANGE THE IF SUITE
# ============================================================

score = 75

if score >= 50:
    print("Passed")

    print("Good job")

print("Result checked")


# ============================================================
# 7. IF + ELSE
# ============================================================

age = 15

if age >= 18:
    print("Can enter")
else:
    print("Cannot enter")


# ============================================================
# 8. IF + ELSE — PREDICTION PRACTICE
# ============================================================

marks = 42

if marks >= 50:
    print("Pass")
else:
    print("Fail")

print("Done")


# ============================================================
# 9. ELIF — MULTIPLE CONNECTED BRANCHES
# ============================================================

marks = 82

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


# ============================================================
# 10. MULTIPLE INDEPENDENT IF STATEMENTS
# ============================================================

marks = 95

if marks >= 90:
    print("Excellent")

if marks >= 75:
    print("Good")

if marks >= 50:
    print("Pass")

if marks < 50:
    print("Fail")


# ============================================================
# 11. AND — BOTH CONDITIONS REQUIRED
# ============================================================

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 12. AND — FIRST CONDITION FALSE
# ============================================================

age = 16
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 13. AND — FIRST CONDITION TRUE, SECOND CONDITION FALSE
# ============================================================

age = 20
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 14. OR — AT LEAST ONE CONDITION REQUIRED
# ============================================================

age = 16
special_permission = True

if age >= 18 or special_permission:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 15. OR — BOTH CONDITIONS FALSE
# ============================================================

age = 16
special_permission = False

if age >= 18 or special_permission:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 16. NOT — NEGATING A BOOLEAN VALUE
# ============================================================

is_raining = False

if not is_raining:
    print("Go outside")
else:
    print("Stay inside")


# ============================================================
# 17. COMBINING AND + NOT
# ============================================================

age = 20
has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 18. LOGICAL OPERATOR PRECEDENCE
# ============================================================

age = 17
has_permission = True
is_banned = False

if age >= 18 or has_permission and not is_banned:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================================
# 19. NESTED IF — BOTH CONDITIONS SATISFIED
# ============================================================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")


# ============================================================
# 20. NESTED IF — OUTER CONDITION FALSE
# ============================================================

age = 16
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")


# ============================================================
# 21. BOUNDARY CONDITION — GREATER THAN
# ============================================================

marks = 50

if marks > 50:
    print("Pass")
else:
    print("Fail")


# ============================================================
# 22. BOUNDARY CONDITION — GREATER THAN OR EQUAL TO
# ============================================================

marks = 50

if marks >= 50:
    print("Pass")
else:
    print("Fail")


# ============================================================
# 23. ASSIGNMENT VS EQUALITY COMPARISON
# ============================================================

age = 18

if age == 18:
    print("Exactly 18")


# ============================================================
# 24. AGE CLASSIFIER — FIRST VERSION
# ============================================================

age = 45

if age > 0 and age <= 13:
    print("Child")

elif age <= 17:
    print("Teenage")

else:
    print("Adult")


# ============================================================
# 25. AGE CLASSIFIER — CORRECTED BOUNDARY
# ============================================================

age = 45

if age > 0 and age < 13:
    print("Child")

elif age <= 17:
    print("Teenage")

else:
    print("Adult")


# ============================================================
# 26. AGE CLASSIFIER — CLEANER FINAL LOGIC
# ============================================================

age = 45

if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")


# ============================================================
# 27. TRUTHINESS — EMPTY STRING
# ============================================================

name = ""

if name:
    print("Name exists")
else:
    print("No name")


# ============================================================
# 28. TRUTHINESS — INTEGER VALUES
# ============================================================

x = 0

if x:
    print("A")
else:
    print("B")


x = 10

if x:
    print("A")
else:
    print("B")


# ============================================================
# 29. TRUTHINESS — STRINGS AND LISTS
# ============================================================

if "":
    print("A")
else:
    print("B")


if "hello":
    print("A")
else:
    print("B")


if []:
    print("A")
else:
    print("B")


if [1, 2]:
    print("A")
else:
    print("B")


# ============================================================
# 30. bool() — TRUTH VALUE OF DIFFERENT VALUES
# ============================================================

print(bool(0))
print(bool(-5))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([0]))


# ============================================================
# 31. MOVIE ENTRY — INDEPENDENT PRACTICAL TASK
# ============================================================

age = 12
parental_permission = False

if age >= 18:
    print("You can watch movie")

elif parental_permission:
    print("You can watch movie")

else:
    print("You Can't watch movie")


# ============================================================
# 32. SHOPPING DISCOUNT — PRACTICAL TASK
# ============================================================

print("SHOP MORE GET MORE DISCOUNT !")

purchase_amount = 4000

discount = 0

if purchase_amount >= 5000:
    discount = 20

elif purchase_amount >= 2000:
    discount = 10

print("Total Discount : ", discount, "%", sep="")


# ============================================================
# 33. DEBUGGING — INCORRECT GRADE ORDER
# ============================================================

marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")
elif marks >= 75:
    print("Good")
else:
    print("Fail")


# ============================================================
# 34. DEBUGGING — CORRECTED GRADE ORDER
# ============================================================

marks = 75

if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


# ============================================================
# 35. GRADE CLASSIFIER — PRACTICAL TASK
# ============================================================

marks = 90

if marks >= 90:
    print("A")

elif marks >= 80:
    print("B")

elif marks >= 70:
    print("C")

elif marks >= 60:
    print("D")

else:
    print("F")


# ============================================================
# 36. DEBUGGING — INCORRECT ENTRY LOGIC
# ============================================================

age = 16
has_permission = False
has_id = True

if age >= 18 or has_permission:
    print("Entry allowed")

elif has_id:
    print("Entry allowed")

else:
    print("Entry denied")


# ============================================================
# 37. DEBUGGING — TWO INDEPENDENT IF STATEMENTS
# ============================================================

age = 16

if age >= 18:
    print("Adult")

if age >= 13:
    print("Teenager")

else:
    print("Child")


# ============================================================
# 38. CORRECTED AGE DECISION CHAIN
# ============================================================

age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# ============================================================
# 39. FINAL PLAYER RANK CLASSIFIER
# ============================================================

player_score = 25

if player_score >= 100:
    print("Legend")

elif player_score >= 75:
    print("Elite")

elif player_score >= 50:
    print("Pro")

elif player_score >= 25:
    print("Rookie")

else:
    print("Beginner")


# ============================================================
# 40. FINAL LESSON 3 — COMBINED CONDITIONAL LOGIC
# ============================================================

age = 16
has_account = True
is_admin = False

if age >= 18 and has_account:
    print("Access granted")

elif is_admin:
    print("Access granted")

else:
    print("Access denied")