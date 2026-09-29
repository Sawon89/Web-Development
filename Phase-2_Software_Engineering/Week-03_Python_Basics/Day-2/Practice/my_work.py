# Week 3 - Day 2 Practice Work
# Topic: Operators, Input/Output & Type Conversion

# Task 1: Basic Calculator
# -------------------------
num1 = 25
num2 = 4

# তোমার কোড নিচে লেখো:
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")
print(f"Power: {num1 ** num2}")


# Task 2: Type Casting
# -------------------------
price = "150"
qty = 3
# তোমার কোড নিচে লেখো:
total_cost = int(price) * qty
print(f"Total Cost is: {total_cost}")



# Task 3: Comparison & Logical Operators
# -------------------------
# তোমার কোড নিচে লেখো:
age = int(input("Enter your age:"))
has_nid = True
can_vote = (age >= 18) and has_nid
print(f"Am i eligable for Vote: {can_vote}")



# Task 4: Bill Splitter App
# -------------------------
# তোমার কোড নিচে লেখো:
print("--- Welcome to Bill Splitter ---")
total_bill =input("Enter the total bill amount: ")
friends = input("Enter the number of friends: ")
tip_percentage = input("Enter the tip percentage: ")

tip_amount =float(total_bill) * (float(tip_percentage) / 100)
total_bill = float(total_bill) + tip_amount
per_person = total_bill / int(friends)
print(f"Total bill (with tip): {total_bill} BDT")
print("Each person should pay: BDT ", per_person)


