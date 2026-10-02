# Day 5 — Lab: Functions (ফাংশন)
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my_work.py`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 6 পাবে।

---

## Lab এর লক্ষ্য
আজকে তুমি:
1. Basic Function তৈরি করবে।
2. Parameters ব্যবহার করে ডাইনামিক ফাংশন বানাবে।
3. `return` ব্যবহার করে ফলাফল ফেরত নেবে।
4. একটি **"Mini Calculator with Functions"** বানাবে! 🧮

---

## Step 1: Practice File খোলো
1. VS Code খোলো
2. এই folder এ যাও: `Phase-2_Software_Engineering/Week-03_Python_Basics/Day-5/Practice/`
3. `my_work.py` file টা খোলো।

---

## Step 2: Tasks (একটা একটা করো)

### ✅ Task 1 — Basic Greeting Function
একটি ফাংশন তৈরি করো যার নাম হবে `welcome_user()`.
- এই ফাংশনটি কোনো প্যারামিটার নেবে না।
- এটি শুধুমাত্র প্রিন্ট করবে: "Welcome to the Python Functions Lab!"
- ফাংশনটি তৈরি করার পর **২ বার** কল করো (ডাকো)।

---

### ✅ Task 2 — Parameters & Arguments
একটি ফাংশন তৈরি করো যার নাম হবে `check_even_odd(number)`.
- এই ফাংশনটি একটি প্যারামিটার `number` নেবে।
- এর ভেতরে `if-else` ব্যবহার করে চেক করবে সংখ্যাটি জোড় না বেজোড় এবং প্রিন্ট করবে।
- ফাংশনটি বানিয়ে **৩ বার** কল করো আলাদা আলাদা সংখ্যা (যেমন: 10, 7, 22) দিয়ে।

---

### ✅ Task 3 — Return Values
একটি ফাংশন তৈরি করো যার নাম হবে `calculate_area(length, width)`.
- এই ফাংশনটি আয়তক্ষেত্রের ক্ষেত্রফল (Area = length * width) হিসাব করবে।
- এটি কিছু `print` করবে না, বরং ফলাফলটি `return` করবে।
- ফাংশনটি কল করে রিটার্ন ভ্যালুটা একটা ভেরিয়েবলে সেভ করো এবং পরে সেটাকে প্রিন্ট করো।

---

### 🌟 Task 4 (Main Project) — Functional Calculator! 🧮
আজকে তুমি একটি ক্যালকুলেটর বানাবে, কিন্তু সবকিছু আলাদা আলাদা ফাংশনের ভেতরে থাকবে!

**ধাপগুলো:**
1. ৪টি আলাদা ফাংশন বানাও:
   - `add(a, b)` -> যোগফল return করবে।
   - `subtract(a, b)` -> বিয়োগফল return করবে।
   - `multiply(a, b)` -> গুণফল return করবে।
   - `divide(a, b)` -> ভাগফল return করবে (খেয়াল রেখো b যেন 0 না হয়, 0 হলে error দেখাবে)।
2. ইউজারের কাছ থেকে দুটো সংখ্যা ইনপুট নাও।
3. ইউজারের কাছ থেকে জানতে চাও সে কী করতে চায় ( +, -, *, / )।
4. ইউজারের পছন্দ অনুযায়ী সঠিক ফাংশনটা কল করে ফলাফল প্রিন্ট করো।

```python
# Hint for structure:
def add(a, b):
    return a + b

# ... বাকি ফাংশনগুলো বানাও ...

# User Input
# num1 = float(input("..."))
# num2 = float(input("..."))
# choice = input("Choose operation (+, -, *, /): ")

# if choice == '+':
#     result = add(num1, num2)
#     print(result)
```

---

## ✅ Lab Checklist
- [ ] Task 1 (Basic Function) করা হয়েছে।
- [ ] Task 2 (Parameters) করা হয়েছে।
- [ ] Task 3 (Return Value) করা হয়েছে।
- [ ] Task 4 (Functional Calculator) ঠিকমতো কাজ করছে।

---

## 🎉 Lab শেষ? এখন কী করবে?
1. `my_work.py` রান করে দেখো সব ঠিকমতো কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 3 - Day 5 lab শেষ করেছি, check করো"**
3. আমি চেক করে Day 6 আনলক করে দেব! 🚀
