# Week 3 - Day 4 Practice Work
# Topic: Loops (for, while)

# Task 1: For Loop & Range (Even Numbers)
# -------------------------
# তোমার কোড নিচে লেখো:
for i in range(0, 51, 2):
    print(i)




# Task 2: Multiplication Table
# -------------------------
# তোমার কোড নিচে লেখো:
num = int(input ("Enter a number:-"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")




# Task 3: Continue & Break
# -------------------------
# তোমার কোড নিচে লেখো:
for num1 in range(1,21):
    if num1==13:
        continue
    elif num1==18:
        break
    else:
        print(num1)
    




# Task 4: Guess the Number Game!
# -------------------------
# তোমার কোড নিচে লেখো:
secret_number =7
while True:
    guess =int(input("Guess the number between 1 to 10:- "))
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")    
    

