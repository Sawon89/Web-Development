# Day 4 — Semantic HTML5
## 📖 Study Material

---

## 1. Semantic HTML কী?

**Semantic** কথাটার মানে হলো "অর্থপূর্ণ"। Semantic tags ব্রাউজার এবং সার্চ ইঞ্জিন (যেমন Google) কে বলে দেয় যে, কোন অংশের কী কাজ। 

আগে মানুষ ওয়েবসাইটের সব অংশ বানানোর জন্য শুধু `<div>` ট্যাগ ব্যবহার করত, যা দেখে বোঝা যেত না কোনটা হেডার, কোনটা ফুটার। Semantic HTML এ নির্দিষ্ট কাজের জন্য নির্দিষ্ট ট্যাগ থাকে।

```
Non-Semantic (আগে যেভাবে করা হতো):    Semantic (এখনকার সঠিক নিয়ম):
<div id="header">             →       <header>
<div id="nav">                →       <nav>
<div id="main">               →       <main>
<div id="footer">             →       <footer>
```

---

## 2. Main Semantic Tags

```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <title>Semantic Page</title>
</head>
<body>

    <!-- সবার উপরে Header অংশ (এখানে সাধারণত লোগো থাকে) -->
    <header>
        <h1>Website এর নাম</h1>
        
        <!-- Navigation Menu -->
        <nav>
            <a href="#home">হোম</a>
            <a href="#about">সম্পর্কে</a>
            <a href="#contact">যোগাযোগ</a>
        </nav>
    </header>

    <!-- মূল content (পেজের আসল বিষয়বস্তু) -->
    <main>

        <!-- একটা Article (যেমন কোনো ব্লগ পোস্ট বা নিউজ) -->
        <article>
            <h2>Semantic HTML কেন শিখব?</h2>
            <p>কারণ এটি এসইও (SEO) এর জন্য ভালো...</p>
        </article>

        <!-- Page Section (পেজের কোনো নির্দিষ্ট অংশ বা বিভাগ) -->
        <section id="about">
            <h2>আমার সম্পর্কে</h2>
            <p>আমি একজন ওয়েব ডেভেলপার...</p>
        </section>

        <!-- Side content (মূল কন্টেন্টের সাথে সম্পর্কিত অতিরিক্ত তথ্য, যেমন সাইডবার) -->
        <aside>
            <h3>Related Links</h3>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
            </ul>
        </aside>

    </main>

    <!-- নিচের Footer অংশ (কপিরাইট, কন্টাক্ট ইনফো) -->
    <footer>
        <p>&copy; 2026. সব অধিকার সংরক্ষিত।</p>
    </footer>

</body>
</html>
```

---

## 3. Semantic Tags এর ব্যবহার

| Tag | কখন ব্যবহার করবে? |
|-----|-----------------|
| `<header>` | ওয়েবসাইট বা কোনো সেকশনের একেবারে উপরের অংশে। |
| `<nav>` | নেভিগেশন মেনু (লিংকগুলো) রাখার জন্য। |
| `<main>` | পেজের প্রধান কনটেন্ট রাখার জন্য। একটি পেজে একবারই ব্যবহার করা উচিত। |
| `<article>` | এমন কন্টেন্ট যা একাই সম্পূর্ণ (যেমন: ব্লগ পোস্ট, নিউজ আর্টিকেল)। |
| `<section>` | পেজের বিভিন্ন বিভাগ বা সেকশন তৈরি করতে। |
| `<aside>` | সাইডবার বা মূল বিষয়ের সাথে সম্পর্কিত অতিরিক্ত তথ্য দেখাতে। |
| `<footer>` | পেজের একেবারে নিচের অংশে (কপিরাইট লেখার জন্য)। |
| `<figure>` | ছবি বা গ্রাফ দেখানোর জন্য। |
| `<figcaption>`| ছবির নিচে ক্যাপশন লেখার জন্য। |

---

## 4. Figure এবং Figcaption

ছবির নিচে ক্যাপশন দেওয়ার জন্য এই ট্যাগগুলো খুব কাজের:

```html
<figure>
    <img src="coding.jpg" alt="কোডিং এর ছবি" width="400">
    <figcaption>চিত্র: একজন ডেভেলপার কোডিং করছে।</figcaption>
</figure>
```

---

## 5. কেন Semantic HTML গুরুত্বপূর্ণ?

1. **SEO (Search Engine Optimization):** Google সহজে বুঝতে পারে তোমার ওয়েবসাইটে কোথায় কী আছে, ফলে সার্চ রেজাল্টে উপরে দেখায়।
2. **Accessibility:** যারা চোখে দেখতে পায় না, তারা স্ক্রিন রিডার (Screen Reader) সফটওয়্যার ব্যবহার করে। Semantic tags থাকলে সফটওয়্যার সহজে ওয়েবসাইট পড়ে শোনাতে পারে।
3. **Maintainability:** কোড দেখতে সুন্দর ও গোছানো হয়, ফলে পরে বুঝতে বা এডিট করতে সুবিধা হয়।

---

## 6. আজকের Summary

✅ Semantic tags অর্থবহ।  
✅ `<header>`, `<nav>`, `<main>`, `<footer>` হলো একটি পেজের মূল কাঠামো।  
✅ `<article>` ব্যবহার হয় স্বয়ংসম্পূর্ণ লেখার জন্য।  
✅ `<div>` এর চেয়ে Semantic ট্যাগ ব্যবহার করা ভালো প্র্যাকটিস।

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
