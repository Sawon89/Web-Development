# আমার Week 3 - Day 1 Practice Work
# Topic: Python Setup + Variables + Data Types
# =========================================
# এই file এ তোমার সব কাজ করো।
# LAB.md দেখে task গুলো একটা একটা করে করো।
# =========================================


# Task 1: এখানে শুরু করো
# -----------------------
# নিচে তোমার code লেখো:


print("Hello! I am learning Python")
print("আমার Software Engineering journey শুরু হলো!")
name = "Saifullah Islam Sawon"
age = 23
city = "Khulna"
dream_job = "Software Engineer"
is_learning = True
#print(f"My Name: {name} and I am {age} years old. I live in {city}" )
print("========== MY ID CARD ==========")  #It shows my Identity
print(f"নাম: {name}")
print(f"বয়স: {age}")
print(f"শহর: {city}")
print(f"স্বপ্নের চাকরি: {dream_job}")
print(f"কি শিখছি: {is_learning}")
print("=================================")

print("Data Types:") # It shows different Data Types
print(type(name))   # String type
print(type(age))    # Integer type
print(type(city))   # String type
print(type(is_learning)) # Boolean type
print(type(dream_job)) # String type

# It takes Input from User
user_name = input("What is your name? : ")
user_age = input("What is your age? : ")
user_city = input("What is your city? : ")

print(f"Hello {user_name}!")
print(f"I am {user_age} years old.")
print(f"I live in {user_city}.")

current_year = 2026
age = int(input("What is your age? : "))
birth_year = current_year - age

print(f"I was born in {birth_year} year.")
print(f"In 2050, I will be: {2050 - birth_year} years old.")