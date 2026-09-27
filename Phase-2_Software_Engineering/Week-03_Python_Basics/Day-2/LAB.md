# Day 2 — Lab: Operators, Input/Output & Type Conversion
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my_work.py`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 3 পাবে।

---

## Lab এর লক্ষ্য
আজকে তুমি:
1. Arithmetic Operator দিয়ে ম্যাথ করবে।
2. Comparison ও Logical operator ব্যবহার করবে।
3. Type Casting (Conversion) করবে।
4. একটি **"Bill Splitter App"** বানাবে! 💸

---

## Step 1: Practice File খোলো
1. VS Code খোলো
2. এই folder এ যাও: `Phase-2_Software_Engineering/Week-03_Python_Basics/Day-2/Practice/`
3. `my_work.py` file টা খোলো।

---

## Step 2: Tasks (একটা একটা করো)

### ✅ Task 1 — Basic Calculator 
দুটি সংখ্যার যোগ, বিয়োগ, গুণ, ভাগ এবং ভাগশেষ (modulus) বের করো।
```python
num1 = 25
num2 = 4

# এখানে +, -, *, /, এবং % ব্যবহার করে ৫টি print statement লেখো
```

---

### ✅ Task 2 — Type Casting 
নিচের কোডটি লেখো এবং error ফিক্স করো Type Conversion ব্যবহার করে:
```python
price = "150"
qty = 3

# Error হবে কারণ String এর সাথে Integer গুণ করা যায় না সরাসরি (String multiply হলে String ই বারবার প্রিন্ট হয়, ম্যাথ হয় না)। 
# price কে int এ convert করে total_cost বের করো।
total_cost = int(price) * qty
print(f"Total Cost is: {total_cost}")
```

---

### ✅ Task 3 — Comparison ও Logical Operators
```python
# তুমি কি ভোট দিতে পারবে? 
age = int(input("Enter your age: "))
has_nid = True

# Logical 'and' এবং Comparison '>=' ব্যবহার করে চেক করো
can_vote = (age >= 18) and has_nid
print(f"Am I eligible to vote? {can_vote}")
```

---

### 🌟 Task 4 (Main Project) — Bill Splitter App!
বন্ধুরা মিলে রেস্টুরেন্টে খেয়েছ। এখন বিল ভাগ করতে হবে। 
- প্রথমে total bill এর input নাও।
- তারপর কয়জন বন্ধু খাবে তার input নাও।
- তারপর tip এর percentage input নাও (যেমন: 10, 15, 20)।
- হিসাব করে বের করো জনপ্রতি কত টাকা দিতে হবে।

```python
print("--- Welcome to Bill Splitter ---")
bill_amount = float(input("Total bill amount: "))
friends = int(input("How many friends? "))
tip_percent = float(input("Tip percentage (e.g., 10, 15): "))

# Calculation
tip_amount = bill_amount * (tip_percent / 100)
total_bill = bill_amount + tip_amount
per_person = total_bill / friends

print("---------------------------------")
print(f"Total bill (with tip): {total_bill} BDT")
print(f"Each person should pay: {per_person} BDT")
```

---

## ✅ Lab Checklist
- [ ] Task 1 (Calculator operators) করা হয়েছে।
- [ ] Task 2 (Type Casting) করা হয়েছে।
- [ ] Task 3 (Logical check) করা হয়েছে।
- [ ] Task 4 (Bill Splitter App) ঠিকমতো কাজ করছে।

---

## 🎉 Lab শেষ? এখন কী করবে?
1. `my_work.py` রান করে দেখো সব ঠিকমতো কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 3 - Day 2 lab শেষ করেছি, check করো"**
3. আমি চেক করে Day 3 আনলক করে দেব! 🚀
