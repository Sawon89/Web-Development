# Day 1 — Lab: Styling a Simple Text Page
## 🧪 হাতে-কলমে Practice (CSS)

---

> ⚠️ **IMPORTANT — Mentor System**
> এই ল্যাব থেকে আমরা HTML এবং CSS দুটো ফাইল নিয়ে কাজ করব।
> তোমার সব কাজ **`Practice/index.html`** এবং **`Practice/style.css`** ফাইলে করতে হবে।
> Lab শেষ হলে আমাকে বলবে, আমি চেক করে Day 2 দেব।

---

## Lab এর লক্ষ্য
আজকে আমরা একটা বেসিক HTML পেজ বানাব এবং আলাদা (External) CSS ফাইল দিয়ে সেটাকে সুন্দর করে ডিজাইন করব।

---

## Step 1: Practice Files খোলো

📂 এই path এ যাও: `Day-1/Practice/`
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
    <title>My First CSS Page</title>
    
    <!-- Task 1: CSS ফাইল লিংক করো -->
    <!-- Hint: <link rel="stylesheet" href="..."> -->
    
</head>
<body>

    <h1 id="main-heading">Welcome to CSS World!</h1>
    
    <p class="intro-text">
        This is my first paragraph. I am learning how to connect HTML with CSS.
    </p>
    
    <p class="highlight-text">
        CSS makes everything look beautiful.
    </p>

    <a href="#" class="my-link">Click Here</a>

</body>
</html>
```

### Task 1 — CSS লিংক করা:
উপরে দেখানো `<head>` এর ভেতরে তোমার `style.css` ফাইলটি লিংক করো।

---

## Step 3: CSS এর কাজ (style.css)

এবার `style.css` ফাইলে যাও এবং নিচের টাস্কগুলো কমপ্লিট করো:

### Task 2 — Body Styling (Element Selector)
পুরো পেজের (body) ব্যাকগ্রাউন্ড কালার হালকা ধূসর করে দাও।
- Background Color: `#f0f0f0`
- Font Family: `Arial, sans-serif`

### Task 3 — Main Heading Styling (ID Selector)
`id="main-heading"` টাকে ডিজাইন করো।
- Text Color: `#2c3e50` (গাঢ় নীল)
- Text Alignment: `center`

### Task 4 — Intro Text (Class Selector)
`class="intro-text"` টাকে ডিজাইন করো।
- Font Size: `20px`
- Text Color: `#34495e`

### Task 5 — Highlight Text (Class Selector)
`class="highlight-text"` টাকে ডিজাইন করো।
- Background Color: `yellow`
- Font Weight: `bold`

### Task 6 — Link Styling (Class Selector)
`class="my-link"` টাকে একটা বাটনের মতো ডিজাইন করো।
- Text Decoration: `none` (আন্ডারলাইন দূর করতে)
- Background Color: `blue`
- Text Color: `white`

---

## ✅ Checklist (নিজে Check করো)

- [ ] `index.html` ফাইলে `style.css` লিংক করা হয়েছে।
- [ ] পেজের ব্যাকগ্রাউন্ড কালার চেঞ্জ হয়েছে।
- [ ] মেইন হেডিং মাঝখানে (center) এসেছে এবং কালার চেঞ্জ হয়েছে।
- [ ] Highlight টেক্সটের ব্যাকগ্রাউন্ড হলুদ হয়েছে।
- [ ] লিংকটির নিচের দাগ (underline) চলে গেছে এবং নীল ব্যাকগ্রাউন্ড পেয়েছে।
- [ ] ব্রাউজারে দেখতে সুন্দর লাগছে।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `index.html` ফাইলটি Live Server এ ওপেন করে দেখো সব স্টাইল কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 2 - Day 1 lab শেষ করেছি, check করো"**।
