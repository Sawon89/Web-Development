# Week 3 - Day 3 Practice Work
# Topic: Conditionals (if / elif / else)

# Task 1: Odd or Even
# -------------------------
# তোমার কোড নিচে লেখো:
num = int(input("Enter a number: "))
if num % 2 ==0 :
    print("The number is Even")
else:
    print("The number is Odd")




# Task 2: Grading System
# -------------------------
# তোমার কোড নিচে লেখো:
mark =int(input("Enter your marks:"))
if mark >=80:
    print("A+")
elif mark >=70:
    print("A")
elif mark >=60:
    print("A-")
elif mark >=50:
    print("B")
else:
    print("F (Fail)")

    



# Task 3: Nested If: Login System
# -------------------------
# তোমার কোড নিচে লেখো:
user_name = input("Enter your name: ").lower()
password = input("Enter your password: ")
if user_name=="admin":
    if password=="12345":
        print("Login Successful!")
    else:
        print("Incorrect Password!")
else:
    print("User not found!")




# Task 4: Text Adventure Game!
# -------------------------
# তোমার কোড নিচে লেখো:
print("Welcome to the Dark Forest Adventure!")
choice1 = input("You are in a dark forest. Do you want to go 'left' or 'right'? ").lower()

if choice1 =="left":
    choice2 =input("You found a bear! Do you want to 'run' or 'hide'? ").lower()
    if choice2 == "run":
        print("You ran away safely! You Win!")
    else:
        print("The bear caught you! Game Over!")

elif choice1 == "right":
    choice3 =input("you found two Mysterious Box!! You have to choose red or green box").lower()
    if choice3 == "red":
        print("You found a Snake inside the red box and Snake bite you and you died! Game Over!")
    elif choice3 =="green":
        print("You found a Treasure inside the green box and you won the Game!")
    else:
        print("You did not choose a valid option. Game Over!")
else:
    print("You did not choose a valid option. Game Over!")  
    


    



