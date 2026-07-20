"""
Python Operators Guide
Comprehensive examples of all operator types in Python
"""

# ============================================================================
# 1. ARITHMETIC OPERATORS
# ============================================================================
print("=" * 50)
print("1. ARITHMETIC OPERATORS")
print("=" * 50)

a = 10
b = 3

print(f"Addition (+): {a} + {b} = {a + b}")              # 13
print(f"Subtraction (-): {a} - {b} = {a - b}")           # 7
print(f"Multiplication (*): {a} * {b} = {a * b}")        # 30
print(f"Division (/): {a} / {b} = {a / b}")              # 3.333...
print(f"Floor Division (//): {a} // {b} = {a // b}")     # 3
print(f"Modulus (%): {a} % {b} = {a % b}")               # 1
print(f"Exponentiation (**): {a} ** {b} = {a ** b}")     # 1000


# ============================================================================
# 2. COMPARISON OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("2. COMPARISON OPERATORS")
print("=" * 50)

x = 5
y = 8

print(f"Equal (==): {x} == {y} = {x == y}")              # False
print(f"Not Equal (!=): {x} != {y} = {x != y}")          # True
print(f"Greater Than (>): {x} > {y} = {x > y}")          # False
print(f"Less Than (<): {x} < {y} = {x < y}")             # True
print(f"Greater or Equal (>=): {x} >= {y} = {x >= y}")   # False
print(f"Less or Equal (<=): {x} <= {y} = {x <= y}")      # True


# ============================================================================
# 3. LOGICAL OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("3. LOGICAL OPERATORS")
print("=" * 50)

p = True
q = False

print(f"AND: {p} and {q} = {p and q}")                   # False
print(f"OR: {p} or {q} = {p or q}")                      # True
print(f"NOT: not {p} = {not p}")                         # False
print(f"NOT: not {q} = {not q}")                         # True

# Logical with numbers
num1 = 10
num2 = 20
print(f"\n{num1} > 5 and {num2} < 30 = {num1 > 5 and num2 < 30}")  # True
print(f"{num1} > 15 or {num2} < 30 = {num1 > 15 or num2 < 30}")   # True


# ============================================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("4. ASSIGNMENT OPERATORS")
print("=" * 50)

n = 10
print(f"Initial value: n = {n}")

n += 5          # n = n + 5
print(f"After n += 5: n = {n}")                          # 15

n -= 3          # n = n - 3
print(f"After n -= 3: n = {n}")                          # 12

n *= 2          # n = n * 2
print(f"After n *= 2: n = {n}")                          # 24

n /= 4          # n = n / 4
print(f"After n /= 4: n = {n}")                          # 6.0

n //= 2         # n = n // 2
print(f"After n //= 2: n = {n}")                         # 3.0

n **= 2         # n = n ** 2
print(f"After n **= 2: n = {n}")                         # 9.0

n %= 5          # n = n % 5
print(f"After n %= 5: n = {n}")                          # 4.0


# ============================================================================
# 5. BITWISE OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("5. BITWISE OPERATORS")
print("=" * 50)

m1 = 12         # Binary: 1100
m2 = 10         # Binary: 1010

print(f"AND (&): {m1} & {m2} = {m1 & m2}")               # 8  (Binary: 1000)
print(f"OR (|): {m1} | {m2} = {m1 | m2}")                # 14 (Binary: 1110)
print(f"XOR (^): {m1} ^ {m2} = {m1 ^ m2}")               # 6  (Binary: 0110)
print(f"NOT (~): ~{m1} = {~m1}")                         # -13
print(f"Left Shift (<<): {m1} << 2 = {m1 << 2}")         # 48 (1100 -> 110000)
print(f"Right Shift (>>): {m1} >> 2 = {m1 >> 2}")        # 3  (1100 -> 11)


# ============================================================================
# 6. IDENTITY OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("6. IDENTITY OPERATORS")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"\nlist1 is list2: {list1 is list2}")              # False (different objects)
print(f"list1 is list3: {list1 is list3}")               # True (same object)
print(f"list1 is not list2: {list1 is not list2}")       # True
print(f"list1 == list2: {list1 == list2}")               # True (same content)


# ============================================================================
# 7. MEMBERSHIP OPERATORS
# ============================================================================
print("\n" + "=" * 50)
print("7. MEMBERSHIP OPERATORS")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]

print(f"List: {fruits}")
print(f"\n'apple' in fruits: {'apple' in fruits}")        # True
print(f"'grape' in fruits: {'grape' in fruits}")         # False
print(f"'banana' not in fruits: {'banana' not in fruits}")  # False
print(f"'orange' not in fruits: {'orange' not in fruits}")  # True

# With strings
text = "Hello World"
print(f"\nText: '{text}'")
print(f"'Hello' in text: {'Hello' in text}")             # True
print(f"'xyz' in text: {'xyz' in text}")                 # False


# ============================================================================
# 8. OPERATOR PRECEDENCE
# ============================================================================
print("\n" + "=" * 50)
print("8. OPERATOR PRECEDENCE")
print("=" * 50)

# Higher precedence operators are evaluated first
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")                          # 14 (not 20)

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")                        # 20

result3 = 10 - 4 - 2
print(f"10 - 4 - 2 = {result3}")                         # 4 (left to right)

result4 = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result4}")                        # 512 (right to left: 2**(3**2))


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("\n" + "=" * 50)
print("9. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Check if number is even and positive
num = 15
if num % 2 == 0 and num > 0:
    print(f"{num} is a positive even number")
else:
    print(f"{num} is not a positive even number")

# Example 2: Swap two variables using operators
val1 = 5
val2 = 10
print(f"\nBefore swap: val1 = {val1}, val2 = {val2}")

val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2
print(f"After swap: val1 = {val1}, val2 = {val2}")

# Example 3: Check grade based on score
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"\nScore: {score}, Grade: {grade}")

# Example 4: Using bitwise for permissions
READ = 1 << 0    # 1 (001)
WRITE = 1 << 1   # 2 (010)
EXECUTE = 1 << 2 # 4 (100)

user_permissions = READ | WRITE  # User has read and write
print(f"\nUser has READ: {bool(user_permissions & READ)}")     # True
print(f"User has WRITE: {bool(user_permissions & WRITE)}")    # True
print(f"User has EXECUTE: {bool(user_permissions & EXECUTE)}")  # False
