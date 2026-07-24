# Day 3 — Lab: Navigation Bar & Flex Cards
## 🧪 হাতে-কলমে Practice (CSS)

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/index.html`** এবং **`Practice/style.css`** ফাইলে করতে হবে।
> Lab শেষ হলে আমাকে বলবে, আমি চেক করে Day 4 দেব।

---

## Lab এর লক্ষ্য
Flexbox ব্যবহার করে আজ আমরা একটা সুন্দর **Navigation Menu (Navbar)** এবং ৩টি **Card** কে পাশাপাশি সাজাবো।

---

## Step 1: Practice Files খোলো

📂 এই path এ যাও: `Day-3/Practice/`
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
    <title>Flexbox Layout</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Navbar Section -->
    <nav class="navbar">
        <div class="logo">MyBrand</div>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <!-- Cards Section -->
    <div class="card-container">
        <div class="card">
            <h3>Card 1</h3>
            <p>Flexbox makes it easy to align items.</p>
        </div>
        <div class="card">
            <h3>Card 2</h3>
            <p>It can align items horizontally and vertically.</p>
        </div>
        <div class="card">
            <h3>Card 3</h3>
            <p>Say goodbye to float and clear properties!</p>
        </div>
    </div>

</body>
</html>
```

---

## Step 3: CSS এর কাজ (style.css)

এবার `style.css` ফাইলে যাও এবং নিচের টাস্কগুলো কমপ্লিট করো:

### Task 1 — Basic Reset
সব এলিমেন্টের ডিফল্ট মার্জিন-প্যাডিং সরাতে নিচের কোডটুকু দাও:
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}
```

### Task 2 — Navbar Flexbox (Class Selector `.navbar`)
ন্যাপবারটাকে ফ্লেক্সবক্স বানাও:
- Background Color: `#333` (গাঢ় ধূসর)
- Text Color: `#fff`
- Padding: `15px 30px`
- **Flexbox ম্যাজিক:** `display: flex;`
- **Justify Content:** `space-between;` (লোগো বামে, লিংক ডানে চলে যাবে!)
- **Align Items:** `center;` (উপরে-নিচে মাঝখানে আসবে)

### Task 3 — Logo Styling (Class Selector `.logo`)
- Font Size: `24px`
- Font Weight: `bold`

### Task 4 — Nav Links Flexbox (Class Selector `.nav-links`)
লিংকগুলোকে পাশাপাশি বসাতে ফ্লেক্সবক্স ব্যবহার করো:
- List Style: `none;` (বুলেট পয়েন্ট দূর করার জন্য)
- **Flexbox ম্যাজিক:** `display: flex;`
- Gap: `20px;` (লিংকগুলোর মাঝে ফাঁকা জায়গা দেওয়ার জন্য ফ্লেক্সবক্সের `gap` খুব কাজের!)

### Task 5 — Nav Link Colors (`.nav-links a`)
- Color: `white`
- Text Decoration: `none`

### Task 6 — Cards Container Flexbox (Class Selector `.card-container`)
৩টা কার্ডকে পাশাপাশি আনতে ফ্লেক্সবক্স ব্যবহার করো:
- **Flexbox ম্যাজিক:** `display: flex;`
- **Justify Content:** `center;`
- Gap: `30px;` (কার্ডগুলোর মাঝে ফাঁকা)
- Padding: `50px`
- Flex Wrap: `wrap;` (স্ক্রিন ছোট হলে যেন কার্ডগুলো নিচে নেমে যায়)

### Task 7 — Card Styling (Class Selector `.card`)
- Background Color: `white`
- Padding: `20px`
- Border Radius: `10px`
- Width: `250px`
- Text Align: `center`
- Box Shadow: `0 4px 8px rgba(0,0,0,0.1);` (কার্ডে একটু ছায়া দেওয়ার জন্য)

---

## ✅ Checklist (নিজে Check করো)

- [ ] নেভিগেশন বারের লোগো বামে এবং লিংকগুলো ডানে এসেছে।
- [ ] লিংকগুলো পাশাপাশি এবং সুন্দর ফাঁকা নিয়ে বসেছে।
- [ ] ৩টি কার্ড পেজের মাঝখানে পাশাপাশি বসেছে।
- [ ] কার্ডগুলোতে হালকা ছায়া (shadow) এবং গোল কোণা এসেছে।
- [ ] ব্রাউজারে দেখতে একদম প্রফেশনাল লেআউটের মতো লাগছে।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `index.html` ফাইলটি Live Server এ ওপেন করে দেখো সব স্টাইল কাজ করছে কিনা।
2. আমাকে বলো: **"আমি Week 2 - Day 3 lab শেষ করেছি, check করো"**।
