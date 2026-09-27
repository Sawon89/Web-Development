# Day 1 — Python কী এবং Variables + Data Types
## 📖 Study Material

---

## 1. Python কী?

**Python** হলো একটি high-level, easy-to-read programming language।

```
ভাবো এভাবে:
- Python = মানুষের ভাষার মতো সহজ
- C/C++ = মেশিনের কাছাকাছি, কঠিন
- Python পড়লে মনে হয় English পড়ছো!
```

### Python কোথায় ব্যবহার হয়?
| ক্ষেত্র | উদাহরণ |
|--------|--------|
| Web Backend | Instagram, Pinterest (Python দিয়ে তৈরি!) |
| Data Science | Netflix recommendation system |
| AI / ML | ChatGPT এর training |
| Automation | Repetitive task automate করা |
| Software Engineering | সব ধরনের software |

---

## 2. Python Setup করো

### Step 1: Python Install
1. [python.org/downloads](https://www.python.org/downloads/) এ যাও
2. Latest version download করো (3.12+)
3. Install করার সময় **"Add Python to PATH"** ✅ tick দিতে ভুলবে না!

### Step 2: Check করো
Terminal/Command Prompt খুলে লেখো:
```
python --version
```
যদি দেখায় `Python 3.x.x` — তাহলে সফল! ✅

### Step 3: VS Code এ Python Extension
1. VS Code খোলো
2. Extensions (Ctrl+Shift+X) এ যাও
3. "Python" লিখে search করো
4. Microsoft এর Python extension install করো

---

## 3. তোমার প্রথম Python Program

একটা নতুন file তৈরি করো: `hello.py`

```python
print("Hello, World!")
print("আমি Python শিখছি!")
```

Run করতে: Terminal এ লেখো `python hello.py`

**Output দেখবে:**
```
Hello, World!
আমি Python শিখছি!
```

> 🎉 Congratulations! তুমি প্রথম Python program লিখে ফেললে!

---

## 4. Variables — তথ্য জমা রাখার বাক্স

**Variable** হলো একটা নামের বাক্স যেখানে data রাখা যায়।

```python
# এভাবে variable তৈরি করে value রাখো:
name = "Sawon"
age = 25
city = "Dhaka"

print(name)   # Output: Sawon
print(age)    # Output: 25
print(city)   # Output: Dhaka
```

### Variable নামের নিয়ম:
| ✅ সঠিক | ❌ ভুল |
|--------|-------|
| `my_name` | `my-name` (hyphen দেওয়া যাবে না) |
| `age25` | `25age` (সংখ্যা দিয়ে শুরু না) |
| `student_count` | `student count` (space দেওয়া যাবে না) |
| `firstName` | `class` (reserved word না) |

```python
# ভালো variable নামের উদাহরণ:
student_name = "Rahim"
total_marks = 450
is_passed = True
```

---

## 5. Data Types — কী ধরনের তথ্য রাখা যায়?

Python এ প্রধান data types:

### 5.1 String (str) — লেখা/text
```python
name = "Sawon Ahmed"       # double quote
city = 'Dhaka'             # single quote ও চলে
message = "আমি শিখছি"     # বাংলাও চলে!

print(type(name))          # Output: <class 'str'>
```

### 5.2 Integer (int) — পূর্ণ সংখ্যা
```python
age = 25
score = 100
year = 2025

print(type(age))           # Output: <class 'int'>
```

### 5.3 Float — দশমিক সংখ্যা
```python
height = 5.9
temperature = 36.6
price = 199.99

print(type(height))        # Output: <class 'float'>
```

### 5.4 Boolean (bool) — True বা False
```python
is_student = True
has_job = False
is_passed = True

print(type(is_student))    # Output: <class 'bool'>
```

### 5.5 একসাথে দেখো:
```python
name = "Sawon"       # str
age = 25             # int
gpa = 3.75           # float
is_active = True     # bool

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(gpa))     # <class 'float'>
print(type(is_active)) # <class 'bool'>
```

---

## 6. print() — Screen এ দেখানো

```python
# শুধু text print
print("Hello!")

# Variable print
name = "Sawon"
print(name)

# Multiple জিনিস একসাথে
print("আমার নাম:", name)
print("আমার বয়স:", 25)

# f-string (সবচেয়ে সুন্দর উপায়!)
age = 25
print(f"আমার নাম {name} এবং বয়স {age}")
# Output: আমার নাম Sawon এবং বয়স 25
```

---

## 7. Comments — Code এ Note লেখা

```python
# এটা একটা single line comment — Python এ # দিয়ে

# Variable তৈরি করছি
name = "Sawon"   # এটা আমার নাম

"""
এটা
multi-line
comment
"""

age = 25
```

> 💡 **Tip:** Comment লেখার অভ্যাস করো। Code বড় হলে comment না থাকলে নিজেই বুঝতে পারবে না!

---

## 8. input() — User এর কাছ থেকে input নেওয়া

```python
# User এর কাছ থেকে তথ্য নাও
name = input("তোমার নাম কী? ")
print(f"হ্যালো, {name}!")

# Run করলে দেখবে:
# তোমার নাম কী? [তুমি লিখবে]
# হ্যালো, [তোমার নাম]!
```

> ⚠️ **Note:** `input()` সবসময় **string** return করে।
> সংখ্যা দরকার হলে convert করতে হবে:
> ```python
> age = int(input("তোমার বয়স কত? "))
> ```

---

## 9. আজকের মূল বিষয়গুলো (Summary)

✅ Python setup সম্পন্ন  
✅ `print()` দিয়ে output দেখানো  
✅ Variable তৈরি করা  
✅ ৪টি প্রধান data type: str, int, float, bool  
✅ `type()` দিয়ে data type চেক করা  
✅ `input()` দিয়ে user এর থেকে data নেওয়া  
✅ Comment লেখা  

---

## 10. অতিরিক্ত Resources (পড়তে পারো, বাধ্যতামূলক না)

- 📚 [Python Official Tutorial](https://docs.python.org/3/tutorial/introduction.html)
- 📺 [freeCodeCamp Python Full Course](https://www.youtube.com/watch?v=rfscVS0vtbw) — শুরু থেকে ১ ঘন্টা দেখো
- 💻 [W3Schools Python](https://www.w3schools.com/python/python_variables.asp)

---

## পরের ধাপ

✅ এই material পড়া শেষ হলে → **[Lab এ যাও](./LAB.md)**
