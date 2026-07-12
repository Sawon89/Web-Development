# Day 5 — Lab: Accessible Webpage তৈরি করো
## 🧪 Accessibility Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my-work.html`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই তুমি Week 1-এর Final Mini Project পাবে!
> কোনো সমস্যা হলে **আমাকে জিজ্ঞেস করো**, এগিয়ে যেও না।

---

## Lab এর লক্ষ্য
আজকে আমরা একদম নতুন কোড লিখব না। তুমি **Day 4** এ যে Portfolio-এর কোডটা লিখেছিলে (যেটা আমি একটু আগে চেক করলাম), সেটাই আজ আমরা Accessibility এবং Best Practices মেনে 100% নিখুঁত করব।

---

## Step 1: Practice File রেডি করো

📂 এই path এ যাও: `Day-5/Practice/my-work.html`
- তোমার **Day 4 এর `my-work.html`** এর সম্পূর্ণ কোডটা কপি করে এনে Day 5 এর এই ফাইলে পেস্ট করো। আমরা এই কোডটাকেই আজ আপডেট করব।

---

## Step 2: Tasks

### Task 1 — HTML Validator দিয়ে চেক করা (Important!)
1. তোমার Day 5 এর `my-work.html` এর সব কোড কপি করো।
2. এই ওয়েবসাইটে যাও: https://validator.w3.org/#validate_by_input
3. কোড পেস্ট করো এবং "Check" বাটনে ক্লিক করো।
4. যদি কোনো Error বা Warning দেখায়, তবে সেগুলো ঠিক করো। (খুব সম্ভবত কোনো Error দেখাবে না, কারণ তুমি Day 4 এ খুব ভালো কোড লিখেছো! তবুও একবার চেক করা ভালো প্র্যাকটিস)।

### Task 2 — Images এর Alt Text ঠিক করা
- তোমার কোডে যে দুটো `<img>` আছে, সেগুলোর `alt` attribute চেক করো। 
- স্ক্রিন রিডার যেন বুঝতে পারে ছবিতে কী আছে, সেভাবে সুন্দর করে `alt` এর লেখাটা একটু বিস্তারিত করে দাও। (যেমন: `alt="A professional photo of Md Saifullah Islam Sawon"`)

### Task 3 — `aria-label` যোগ করা
- তোমার `<nav>` এর ভেতরে সোশ্যাল মিডিয়া লিংকগুলো (Google, YouTube, LinkedIn, Facebook, Github) আছে। 
- এই লিংকগুলোতে `aria-label` যুক্ত করো। (যেমন: `<a href="https://www.linkedin.com" target="_blank" aria-label="Visit my LinkedIn Profile">Go to Linkedin</a>`)

### Task 4 — Skip Navigation যোগ করা (Keyboard Accessibility)
যাঁরা মাউস ব্যবহার করতে পারেন না, তাঁদের সুবিধার জন্য হেডারের ঠিক আগে (অর্থাৎ `<body>` ট্যাগের ঠিক পরেই) এই কোডটুকু যোগ করো:
```html
<a href="#about" tabindex="0">Skip to About section</a>
```
(এটা কীবোর্ডের 'Tab' প্রেস করলে ফোকাস পাবে)।

---

## ✅ Checklist (নিজে Check করো)

- [ ] W3C Validator-এ কোড চেক করেছো এবং কোনো Error নেই।
- [ ] সবগুলো ছবির `alt` text সুন্দরভাবে বিস্তারিত লেখা হয়েছে।
- [ ] সোশ্যাল লিংকে `aria-label` যুক্ত করেছো।
- [ ] `<body>` এর পরপরই Skip Navigation লিংক যুক্ত করেছো।

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `Practice/my-work.html` file টা Browser এ দেখো। 
2. নিজে checklist এর সব tick করো
3. আমাকে বলো: **"আমি Day 5 lab শেষ করেছি, check করো"**
4. আমি তোমার কাজ দেখব এবং feedback দেব

সব ঠিক থাকলে তুমি **Week 1-এর Final Mini Project** পাবে! 🏆
