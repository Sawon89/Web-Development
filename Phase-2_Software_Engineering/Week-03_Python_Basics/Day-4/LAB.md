# Day 4 — Lab: Loops (for, while)
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my_work.py`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 5 পাবে।

---

## Lab এর লক্ষ্য
আজকে তুমি:
1. `for loop` এবং `range()` দিয়ে সংখ্যার প্যাটার্ন প্রিন্ট করবে।
2. `while loop` দিয়ে কন্ডিশনাল লুপ বানাবে।
3. `break` এবং `continue` এর প্র্যাকটিক্যাল ব্যবহার শিখবে।
4. একটি **"Guess the Number"** গেম বানাবে! 🎯

---

## Step 1: Practice File খোলো
1. VS Code খোলো
2. এই folder এ যাও: `Phase-2_Software_Engineering/Week-03_Python_Basics/Day-4/Practice/`
3. `my_work.py` file টা খোলো।

---

## Step 2: Tasks (একটা একটা করো)

### ✅ Task 1 — For Loop & Range
একটি `for loop` এবং `range()` ব্যবহার করে ১ থেকে ৫০ এর মধ্যে থাকা **শুধুমাত্র জোড় সংখ্যাগুলো (Even numbers)** প্রিন্ট করো।

```python
# Hint: range(start, stop, step) 
```

---

### ✅ Task 2 — Multiplication Table (নামতা)
ইউজারের কাছ থেকে একটি সংখ্যা ইনপুট নাও। তারপর `for loop` ব্যবহার করে ওই সংখ্যার নামতা (Multiplication table) ১ থেকে ১০ পর্যন্ত প্রিন্ট করো।

*Output Example (যদি ইউজার 5 দেয়):*
```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

### ✅ Task 3 — Continue & Break
১ থেকে ২০ পর্যন্ত একটি `for loop` চালাও। 
- যদি সংখ্যাটি ১৩ হয়, তবে `continue` করে স্কিপ করো (১৩ প্রিন্ট হবে না)।
- যদি সংখ্যাটি ১৮ হয়, তবে `break` করে লুপ থামিয়ে দাও।
- বাকি সব সংখ্যা প্রিন্ট করো।

---

### 🌟 Task 4 (Main Project) — Guess the Number Game! 🎲
একটি দারুণ গেম বানাবে! 
- প্রোগ্রামের ভেতরে একটি Secret Number সেট করো (যেমন: `secret_number = 7`)
- ইউজারকে বল সংখ্যাটা অনুমান করতে (Guess the number between 1 to 10)।
- একটি `while loop` ব্যবহার করো যাতে ইউজার যতক্ষণ সঠিক উত্তর না দেয়, ততক্ষণ সে আবার ইনপুট দেওয়ার সুযোগ পায়।
- যদি সে ঠিক অনুমান করে, তাহলে প্রিন্ট করো "Congratulations! You guessed it right!" এবং `break` দিয়ে লুপ থামিয়ে দাও।

> **Pro Tip:** তুমি চাইলে ইউজারকে Hint ও দিতে পারো। যেমন ইউজার যদি ৩ দেয়, তুমি প্রিন্ট করতে পারো "Too low! Try again." আর যদি ৯ দেয়, বলতে পারো "Too high! Try again." 

---

## ✅ Lab Checklist
- [ ] Task 1 (Even numbers) করা হয়েছে।
- [ ] Task 2 (Multiplication Table) করা হয়েছে।
- [ ] Task 3 (Continue/Break) করা হয়েছে।
- [ ] Task 4 (Guess the Number) ঠিকমতো কাজ করছে।

---

## 🎉 Lab শেষ? এখন কী করবে?
1. `my_work.py` রান করে দেখো সব ঠিকমতো কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 3 - Day 4 lab শেষ করেছি, check করো"**
3. আমি চেক করে Day 5 আনলক করে দেব! 🚀
