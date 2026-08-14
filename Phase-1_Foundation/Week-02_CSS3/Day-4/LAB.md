# Day 4 — Lab: CSS Grid Photo Gallery
## 🧪 হাতে-কলমে Practice (CSS)

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/index.html`** এবং **`Practice/style.css`** ফাইলে করতে হবে।
> Lab শেষ হলে আমাকে বলবে, আমি চেক করে Day 5 দেব।

---

## Lab এর লক্ষ্য
CSS Grid ব্যবহার করে আজ আমরা একটা সুন্দর **Photo Gallery** তৈরি করব, যা স্ক্রিনের সাইজ অনুযায়ী নিজে নিজেই কলাম সংখ্যা পরিবর্তন করবে (Responsive)!

---

## Step 1: Practice Files খোলো

📂 এই path এ যাও: `Day-4/Practice/`
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
    <title>CSS Grid Photo Gallery</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header class="header">
        <h1>My Awesome Photo Gallery</h1>
        <p>Built with CSS Grid Magic!</p>
    </header>

    <main class="gallery">
        <div class="photo">1</div>
        <div class="photo">2</div>
        <div class="photo">3</div>
        <div class="photo">4</div>
        <div class="photo">5</div>
        <div class="photo">6</div>
        <div class="photo">7</div>
        <div class="photo">8</div>
    </main>

</body>
</html>
```

---

## Step 3: CSS এর কাজ (style.css)

এবার `style.css` ফাইলে যাও এবং নিচের টাস্কগুলো কমপ্লিট করো:

### Task 1 — Basic Settings
পেজের বেসিক স্টাইল দাও:
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f8f9fa;
}
```

### Task 2 — Header Styling (`.header`)
- Background Color: `#2c3e50`
- Color: `#ffffff`
- Text Align: `center`
- Padding: `40px 20px`
- Margin Bottom: `30px`

### Task 3 — The Grid Magic! (`.gallery`)
এই অংশটাই আসল! `main` ট্যাগটাকে গ্রিড বানাও:
- **Display:** `grid;`
- **Grid Template Columns:** `repeat(auto-fit, minmax(200px, 1fr));` (এই জাদুকরী কোডটা দিয়ে দাও)
- **Gap:** `15px;` (ছবির মাঝে ফাঁকা জায়গা)
- **Padding:** `20px;`

### Task 4 — Photo Items Styling (`.photo`)
গ্যালারির ভেতরের বক্সগুলোকে সুন্দর করো (আমরা এখানে আসল ছবির বদলে বক্স বানাচ্ছি):
- Background Color: `#3498db`
- Color: `#ffffff`
- Font Size: `30px`
- Font Weight: `bold`
- Text Align: `center`
- **Padding:** উপরে-নিচে `80px` (যাতে বক্সগুলো একটু বড় হয়)
- Border Radius: `10px`
- Box Shadow: `0 4px 6px rgba(0,0,0,0.1)`

---

## ✅ Checklist (নিজে Check করো)

- [ ] Header-টি গাঢ় নীল রঙের এবং লেখা মাঝখানে এসেছে।
- [ ] গ্যালারির বক্সগুলো পাশাপাশি গ্রিড আকারে বসেছে।
- [ ] 브াউজারের উইন্ডো ছোট-বড় করে দেখো—বক্সগুলো কি নিজে থেকেই নিচে নেমে যাচ্ছে বা উপরে উঠে আসছে? (এটাই `auto-fit` এর ম্যাজিক!)
- [ ] বক্সগুলোর কোণা গোল এবং হালকা ছায়া আছে।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `index.html` ফাইলটি Live Server এ ওপেন করে দেখো সব ঠিক আছে কিনা।
2. উইন্ডো ছোট-বড় করে Grid-এর আসল ম্যাজিকটা ফিল করো!
3. আমাকে বলো: **"আমি Week 2 - Day 4 lab শেষ করেছি, check করো"**।
