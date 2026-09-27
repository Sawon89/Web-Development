# Day 1 — Lab: Python Setup + Variables + Data Types
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my_work.py`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 2 পাবে।
> কোনো সমস্যা হলে **আমাকে জিজ্ঞেস করো**, এগিয়ে যেও না।

---

## Lab এর লক্ষ্য

আজকে তুমি:
1. Python সফলভাবে install ও run করবে
2. নিজের information দিয়ে variables তৈরি করবে
3. বিভিন্ন data types নিয়ে কাজ করবে
4. একটা ছোট্ট "Digital ID Card" program বানাবে! 🪪

---

## Step 1: Practice File খোলো

📂 এই path এ যাও: `Day-1/Practice/my_work.py`

1. VS Code খোলো
2. এই folder এ যাও: `Phase-2_Software_Engineering/Week-03_Python_Basics/Day-1/Practice/`
3. `my_work.py` file টা খোলো

---

## Step 2: Python Run করতে শেখো

Terminal খোলো (VS Code এ `Ctrl + ~`) এবং লেখো:
```
python Practice/my_work.py
```

অথবা VS Code এ উপরে ▶️ Run button এ click করো।

---

## Step 3: Tasks (একটা একটা করো)

### ✅ Task 1 — Python সফলভাবে চলছে কিনা দেখো (Beginner)

`my_work.py` তে এটা লেখো:
```python
print("হ্যালো! আমি Python শিখছি!")
print("আমার Software Engineering journey শুরু হলো!")
```

**Terminal এ run করো এবং output দেখো।**

---

### ✅ Task 2 — নিজের Digital ID Card তৈরি করো

নিচের code লেখো কিন্তু **`[এখানে তোমার নাম]` জায়গায় তোমার আসল তথ্য দাও:**

```python
# আমার Digital ID Card
name = "[এখানে তোমার নাম]"
age = 0   # তোমার বয়স দাও
city = "[তোমার শহর]"
dream_job = "Software Engineer"
is_learning = True

print("========== MY ID CARD ==========")
print(f"নাম: {name}")
print(f"বয়স: {age}")
print(f"শহর: {city}")
print(f"স্বপ্নের চাকরি: {dream_job}")
print(f"কি শিখছি: {is_learning}")
print("=================================")
```

**Run করো — তোমার ID Card দেখা যাবে!**

---

### ✅ Task 3 — Data Types চেক করো

```python
# প্রতিটা variable এর type print করো
name = "Sawon"     # তোমার নাম দাও
age = 25           # তোমার বয়স দাও
gpa = 3.75         # তোমার GPA অথবা যেকোনো decimal number
is_student = True  # তুমি কি এখনো student?

print("Data Types:")
print(type(name))       # <class 'str'> দেখাবে
print(type(age))        # <class 'int'> দেখাবে
print(type(gpa))        # <class 'float'> দেখাবে
print(type(is_student)) # <class 'bool'> দেখাবে
```

---

### ✅ Task 4 — User এর থেকে Input নাও

```python
# User এর কাছ থেকে তথ্য নাও
user_name = input("তোমার নাম কী? ")
user_age = int(input("তোমার বয়স কত? "))

print(f"\nহ্যালো {user_name}!")
print(f"তুমি {user_age} বছর বয়সী।")
print(f"আরো {25 - user_age} বছর পরে তুমি ২৫ হবে!")
```

> **Note:** `int()` ব্যবহার করেছি কারণ `input()` সবসময় string দেয়, কিন্তু বয়স দিয়ে math করতে হলে int দরকার।

---

### ✅ Task 5 — Comments দিয়ে Code সাজাও

তোমার **Task 2** এর code এ কমপক্ষে **৫টি comment** যোগ করো।

উদাহরণ:
```python
# এটা আমার Personal Information Section
name = "Sawon"  # String type — লেখা রাখে

# এটা আমার বয়স — Integer type
age = 25
```

---

### 🌟 Bonus Task — Math করো!

```python
# তোমার জন্মসাল বের করো
current_year = 2026
age = int(input("তোমার বয়স কত? "))
birth_year = current_year - age

print(f"তুমি {birth_year} সালে জন্মগ্রহণ করেছো।")
print(f"২০৫০ সালে তোমার বয়স হবে: {2050 - birth_year}")
```

---

## ✅ Lab Checklist

Lab শেষ করার আগে নিচের সব check করো:

- [ ] `print()` সফলভাবে কাজ করছে
- [ ] নিজের তথ্য দিয়ে **ID Card** তৈরি হয়েছে
- [ ] `str`, `int`, `float`, `bool` — ৪টি type use করেছো
- [ ] `type()` দিয়ে type print করেছো
- [ ] `input()` দিয়ে user এর data নিয়েছো
- [ ] কমপক্ষে **৫টি comment** লিখেছো
- [ ] সব code run করেছো এবং error নেই

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `Practice/my_work.py` file টা run করো — সব ঠিক আছে কিনা দেখো
2. নিজে checklist এর সব tick করো
3. আমাকে বলো: **"আমি Week 3 - Day 1 lab শেষ করেছি, check করো"**
4. আমি তোমার কাজ দেখব এবং feedback দেব
5. সব ঠিক থাকলে Day 2 পাবে — না হলে কোথায় ভুল সেটা বলব

**⛔ Day 2 এর material আপাতত নেই — Lab পাস করলে পাবে!**

**কোনো সমস্যা হলে আমাকে জিজ্ঞেস করো** 💬
