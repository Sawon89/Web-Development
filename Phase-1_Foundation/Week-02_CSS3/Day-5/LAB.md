# Day 5 — Lab: Responsive Mobile-Friendly Webpage
## 🧪 হাতে-কলমে Practice (CSS)

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/index.html`** এবং **`Practice/style.css`** ফাইলে করতে হবে।
> Lab শেষ হলে আমাকে বলবে, আমি চেক করে তোমাকে Week 2-এর Final Project দেব।

---

## Lab এর লক্ষ্য
আজকে আমরা একটি বেসিক লেআউট (Navbar এবং Content) তৈরি করব এবং **Media Queries** ব্যবহার করে সেটাকে মোবাইলের জন্য রেসপন্সিভ করব। 
ল্যাপটপে লিংকগুলো পাশাপাশি থাকবে, আর মোবাইলে নিচে-নিচে চলে আসবে!

---

## Step 1: Practice Files খোলো

📂 এই path এ যাও: `Day-5/Practice/`
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
    <title>Responsive Webpage</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Header & Navbar -->
    <header class="header">
        <h1 class="logo">MyBrand</h1>
        <nav class="nav-links">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </nav>
    </header>

    <!-- Main Content -->
    <main class="content">
        <h2>Welcome to Responsive Design</h2>
        <p>Resize the browser window to see the magic of Media Queries!</p>
        <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085" alt="Laptop on desk" class="responsive-img">
    </main>

</body>
</html>
```

---

## Step 3: CSS এর কাজ (style.css)

এবার `style.css` ফাইলে যাও এবং নিচের টাস্কগুলো কমপ্লিট করো:

### Task 1 — Basic Settings ও Image
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

/* ছবি যেন কন্টেইনারের বাইরে না যায় */
.responsive-img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    margin-top: 20px;
}
```

### Task 2 — Desktop Design (বড় স্ক্রিন)
ল্যাপটপের জন্য ডিজাইন:
```css
/* হেডারটাকে ফ্লেক্সবক্স দিয়ে পাশাপাশি রাখছি */
.header {
    background-color: #333;
    color: white;
    padding: 20px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* লিংকগুলোর ডিজাইন */
.nav-links a {
    color: white;
    text-decoration: none;
    margin-left: 20px;
    font-size: 18px;
}

.content {
    padding: 40px;
    text-align: center;
}
```

### Task 3 — Mobile Design (Media Query ম্যাজিক!)
এবার আসল কাজ! যখন স্ক্রিন ছোট (মোবাইল) হবে, তখন নেভিগেশন বারটা কেমন হবে সেটা বলে দাও:

```css
/* যখন স্ক্রিন 768px বা তার চেয়ে ছোট হবে */
@media (max-width: 768px) {
    
    /* হেডার আর পাশাপাশি থাকবে না, নিচে-নিচে আসবে */
    .header {
        flex-direction: column;
        padding: 15px;
    }

    /* লোগোর নিচে একটু ফাঁকা জায়গা দিচ্ছি */
    .logo {
        margin-bottom: 15px;
    }

    /* লিংকগুলোও নিচে-নিচে ব্লক আকারে আসবে এবং মাঝখানে থাকবে */
    .nav-links {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .nav-links a {
        margin: 5px 0;
        padding: 10px;
        background-color: #444;
        text-align: center;
        border-radius: 5px;
    }
}
```

---

## ✅ Checklist (নিজে Check করো)

- [ ] ফুলস্ক্রিনে (ল্যাপটপ মোডে) লোগো বামে এবং লিংকগুলো ডানে আছে।
- [ ] ব্রাউজারের উইন্ডো ছোট (৭৬৮ পিক্সেলের কম) করলে লোগো এবং লিংকগুলো নিজে থেকেই নিচে-নিচে চলে আসছে।
- [ ] ছোট স্ক্রিনে লিংকগুলো সুন্দর বাটন-এর মতো ব্যাকগ্রাউন্ড পাচ্ছে।
- [ ] ছবিটি স্ক্রিন ছোট করার সাথে সাথে ছোট হচ্ছে এবং বাইরে চলে যাচ্ছে না।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `index.html` ফাইলটি Live Server এ ওপেন করো।
2. উইন্ডো ছোট-বড় করে Media Query-এর আসল ম্যাজিকটা ফিল করো!
3. আমাকে বলো: **"আমি Week 2 - Day 5 lab শেষ করেছি, check করো"**।
