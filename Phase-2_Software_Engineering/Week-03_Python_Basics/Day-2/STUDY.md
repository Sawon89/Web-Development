# Day 2 — Operators, I/O এবং Type Conversion
## 📖 Study Material

---

## 1. Operators কী?
Operators হলো কিছু symbols (যেমন +, -, *, /) যা variable বা values এর উপর কাজ (operation) করতে ব্যবহৃত হয়। 

Python এ প্রধানত কয়েক ধরনের Operator আছে:

### 1.1 Arithmetic Operators (গণিত করার জন্য)
```python
x = 10
y = 3

print(x + y)  # 13 (যোগ)
print(x - y)  # 7  (বিয়োগ)
print(x * y)  # 30 (গুণ)
print(x / y)  # 3.333... (ভাগ - সবসময় Float দেয়)
print(x // y) # 3  (Floor Division - ভাগফল শুধু পূর্ণসংখ্যায় দেয়)
print(x % y)  # 1  (Modulus - ভাগশেষ বের করে)
print(x ** y) # 1000 (Exponent - পাওয়ার বা x^y)
```

### 1.2 Assignment Operators (মান বসানোর জন্য)
```python
x = 5     # x এর মান ৫
x += 2    # মানে x = x + 2 (এখন x এর মান 7)
x -= 1    # মানে x = x - 1 (এখন x এর মান 6)
x *= 2    # মানে x = x * 2 (এখন x এর মান 12)
```

### 1.3 Comparison Operators (তুলনা করার জন্য) 
এগুলোর উত্তর সবসময় **True** অথবা **False** আসে।
```python
a = 10
b = 20

print(a == b)  # False (সমান কি না?)
print(a != b)  # True (অসমান কি না?)
print(a > b)   # False (a কি b এর চেয়ে বড়?)
print(a < b)   # True (a কি b এর চেয়ে ছোট?)
print(a >= 10) # True (বড় অথবা সমান?)
```

### 1.4 Logical Operators (শর্ত মেলানোর জন্য)
- **and**: দুটো শর্তই সত্যি হলে True.
- **or**: যেকোনো একটি শর্ত সত্যি হলেই True.
- **not**: উল্টে দেয় (True কে False, False কে True বানায়).

```python
x = 5
print(x > 3 and x < 10) # True (দুটোই সত্যি)
print(x > 3 or x < 4)   # True (প্রথমটা সত্যি)
print(not(x > 3))       # False (x > 3 সত্যি ছিল, not সেটাকে উল্টে দিল)
```

---

## 2. Type Conversion (এক Data Type থেকে অন্যটায় বদলানো)

আমরা Day 1 এ দেখেছিলাম `input()` সবসময় String দেয়। String দিয়ে তো আর Math করা যায় না। তাই একে Number (int/float) এ বদলাতে হয়। একে বলে **Type Conversion বা Casting**।

### 2.1 Implicit Conversion (Python নিজে নিজে করে)
```python
num_int = 10     # integer
num_float = 2.5  # float

result = num_int + num_float
print(type(result)) # <class 'float'> (Python নিজে থেকেই একে float বানিয়ে নিয়েছে)
```

### 2.2 Explicit Conversion (আমাদের নিজেকে করতে হয়)
```python
# String কে Integer এ বদলানো
age_str = "25"
age_int = int(age_str)

# Number কে String এ বদলানো
price = 150
price_str = str(price)
print("The price is " + price_str) 

# Float এ বদলানো
val = float("5.75")
```

---

## 3. Input & Output (Advanced)

```python
# Multiple Input এক লাইনে নেওয়া (একটু advanced কিন্তু কাজে লাগবে)
# split() space অনুযায়ী ভাগ করে নেয়
x, y = input("Enter two numbers (space separated): ").split()
print(int(x) + int(y))
```

---

## 4. আজকের মূল বিষয়গুলো (Summary)
✅ **Arithmetic:** +, -, *, /, //, %, **  
✅ **Assignment:** =, +=, -=, *=, /=  
✅ **Comparison:** ==, !=, >, <, >=, <=  
✅ **Logical:** and, or, not  
✅ **Type Conversion:** int(), str(), float()  

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[Lab এ যাও](./LAB.md)**
