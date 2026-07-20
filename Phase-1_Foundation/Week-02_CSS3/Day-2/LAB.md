# Day 2 — Lab: Creating Styled Cards (Box Model)
## 🧪 হাতে-কলমে Practice (CSS)

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/index.html`** এবং **`Practice/style.css`** ফাইলে করতে হবে।
> Lab শেষ হলে আমাকে বলবে, আমি চেক করে Day 3 দেব।

---

## Lab এর লক্ষ্য
আজকে আমরা Box Model (Margin, Padding, Border) ব্যবহার করে সুন্দর একটা "Profile Card" ডিজাইন করব। 

---

## Step 1: Practice Files খোলো

📂 এই path এ যাও: `Day-2/Practice/`
এখানে দুইটা ফাইল আছে: `index.html` এবং `style.css`।

---

## Step 2: HTML এর কাজ (index.html)

`index.html` ফাইলে নিচের কোডটুকু লেখো (বা কপি-পেস্ট করো):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Box Model Profile Card</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="profile-card">
        <h2 class="name">Md Saifullah Islam Sawon</h2>
        <p class="bio">I am an aspiring Full-Stack Web Developer passionate about coding and building modern applications.</p>
        <a href="#" class="btn">Hire Me</a>
    </div>

</body>
</html>
```

---

## Step 3: CSS এর কাজ (style.css)

এবার `style.css` ফাইলে যাও এবং নিচের টাস্কগুলো কমপ্লিট করো:

### Task 1 — Body Styling
পুরো পেজের ব্যাকগ্রাউন্ড কালার চেঞ্জ করো।
- Background Color: `#e9ecef` (হালকা ধূসর)
- Font Family: `Arial, sans-serif`

### Task 2 — Profile Card Styling (Class Selector `.profile-card`)
কার্ডটিকে ডিজাইন করো (এখানেই আসল Box Model-এর কাজ!):
- Background Color: `#ffffff` (সাদা)
- Width: `350px`
- **Padding:** চারদিকে `30px` দাও।
- **Margin:** উপরে-নিচে `50px` এবং ডানে-বামে `auto` দাও (যাতে কার্ডটা পেজের মাঝখানে আসে)।
- **Border:** `2px solid #3498db` (নীল রঙের বর্ডার) দাও।
- **Border Radius:** `15px` (কোণাগুলো গোল করার জন্য)।
- Text Align: `center` (সব লেখা মাঝখানে আনতে)।

### Task 3 — Name Styling (Class Selector `.name`)
- Text Color: `#2c3e50` (গাঢ় নীল)
- Margin Bottom: `10px` (নিচের দিকে ১০ পিক্সেল ফাঁকা জায়গা দাও)

### Task 4 — Bio Styling (Class Selector `.bio`)
- Text Color: `#7f8c8d` (হালকা ধূসর)
- Line Height: `1.6`
- Margin Bottom: `25px` (নিচের দিকে ২৫ পিক্সেল ফাঁকা জায়গা দাও)

### Task 5 — Button Styling (Class Selector `.btn`)
বাটনটাকে ডিজাইন করো:
- Text Decoration: `none`
- Background Color: `#3498db`
- Text Color: `#ffffff`
- **Padding:** উপরে-নিচে `10px`, ডানে-বামে `20px` দাও।
- **Border Radius:** `25px` (কোণা বেশ গোল হবে)।

---

## ✅ Checklist (নিজে Check করো)

- [ ] কার্ডটির চারদিকে বর্ডার এবং গোল কোণা এসেছে।
- [ ] `padding` দেওয়ার কারণে লেখার চারদিকে ফাঁকা জায়গা তৈরি হয়েছে।
- [ ] `margin: 50px auto;` ব্যবহার করার কারণে কার্ডটি পেজের ঠিক মাঝখানে চলে এসেছে।
- [ ] "Hire Me" লেখাটি একটা সুন্দর বাটনের মতো দেখাচ্ছে, যার চারদিকে `padding` এবং `border-radius` আছে।
- [ ] ব্রাউজারে দেখতে সুন্দর লাগছে।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `index.html` ফাইলটি Live Server এ ওপেন করে দেখো সব স্টাইল কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 2 - Day 2 lab শেষ করেছি, check করো"**।
