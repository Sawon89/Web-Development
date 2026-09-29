# Day 3 — Lab: Conditionals (if / elif / else)
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my_work.py`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 4 পাবে।

---

## Lab এর লক্ষ্য
আজকে তুমি:
1. `if - else` দিয়ে সাধারণ লজিক বানাবে।
2. `if - elif - else` দিয়ে মাল্টিপল কন্ডিশন হ্যান্ডেল করবে।
3. Logical operator (and/or) দিয়ে শর্ত যাচাই করবে।
4. একটি **"Interactive Mini Game"** বানাবে! 🎮

---

## Step 1: Practice File খোলো
1. VS Code খোলো
2. এই folder এ যাও: `Phase-2_Software_Engineering/Week-03_Python_Basics/Day-3/Practice/`
3. `my_work.py` file টা খোলো।

---

## Step 2: Tasks (একটা একটা করো)

### ✅ Task 1 — Odd or Even (জোড় না বেজোড়?)
ইউজারের কাছ থেকে একটি সংখ্যা নাও। এরপর `if - else` এবং Modulus (`%`) ব্যবহার করে চেক করো সংখ্যাটি জোড় নাকি বেজোড়।

```python
# Hint: কোনো সংখ্যা ২ দিয়ে ভাগ করলে ভাগশেষ ০ হলে সেটা জোড় (Even), না হলে বেজোড় (Odd)।
```

---

### ✅ Task 2 — Grading System
ইউজারের কাছ থেকে তার প্রাপ্ত মার্কস (0 থেকে 100) ইনপুট নাও। তারপর `if - elif - else` দিয়ে গ্রেড বের করো।
- 80 বা তার বেশি: "A+"
- 70-79: "A"
- 60-69: "A-"
- 50-59: "B"
- 50 এর কম: "F (Fail)"

---

### ✅ Task 3 — Nested If: Login System
ধরে নাও, তোমার সিস্টেমে সঠিক Username হলো `"admin"` এবং Password হলো `"12345"`।
ইউজারের কাছ থেকে username এবং password ইনপুট নাও।

- প্রথমে চেক করো username ঠিক আছে কি না।
    - যদি ঠিক থাকে, তাহলে ভেতরে (nested if) গিয়ে password চেক করো।
        - password ঠিক হলে প্রিন্ট করো: "Login Successful!"
        - ভুল হলে প্রিন্ট করো: "Incorrect Password!"
    - যদি username ভুল হয়, তাহলে প্রিন্ট করো: "User not found!"

---

### 🌟 Task 4 (Main Project) — Text Adventure Game! 🗺️
একটি ছোট গেম বানাও। যেখানে ইউজারকে সিদ্ধান্ত নিতে হবে। 

গল্পটা এমন:
তুমি একটা অন্ধকার জঙ্গলে আছো। তোমার সামনে দুটো রাস্তা: "left" এবং "right"।
- যদি ইউজার "left" লেখে, তবে সে একটা ভাল্লুকের সামনে পড়বে। 
    - ভাল্লুক দেখে সে কী করবে? "run" নাকি "hide"? 
        - "run" লিখলে: "তুমি দৌড়ে বেঁচে গেলে! You Win!"
        - "hide" লিখলে: "ভাল্লুক তোমাকে খুঁজে পেয়েছে! Game Over!"
- যদি ইউজার "right" লেখে, তবে সে একটা গুপ্তধন পাবে। প্রিন্ট করো: "তুমি গুপ্তধন পেয়েছ! You Win!"
- যদি ইউজার left/right বাদে অন্য কিছু লেখে, তবে সে গর্তে পড়ে যাবে। প্রিন্ট করো: "Game Over!"

> **Hint:** ইউজারের ইনপুট String হবে, তাই `if user_choice == "left":` এভাবে কন্ডিশন দেবে। `input().lower()` ব্যবহার করলে ইউজারের সব লেখা ছোট হাতের (lowercase) হয়ে যাবে, এতে কন্ডিশন মেলাতে সুবিধা হবে।

---

## ✅ Lab Checklist
- [ ] Task 1 (Odd/Even) করা হয়েছে।
- [ ] Task 2 (Grading System) করা হয়েছে।
- [ ] Task 3 (Login System with Nested If) করা হয়েছে।
- [ ] Task 4 (Adventure Game) ঠিকমতো কাজ করছে।

---

## 🎉 Lab শেষ? এখন কী করবে?
1. `my_work.py` রান করে দেখো সব ঠিকমতো কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 3 - Day 3 lab শেষ করেছি, check করো"**
3. আমি চেক করে Day 4 আনলক করে দেব! 🚀
