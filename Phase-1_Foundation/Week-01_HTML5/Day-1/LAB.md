# Day 1 — Lab: Personal Introduction Page
## 🧪 হাতে-কলমে Practice

---

> ⚠️ **IMPORTANT — Mentor System**
> তোমার সব কাজ **`Practice/my-work.html`** file এ করতে হবে।
> Lab শেষ হলে আমাকে বলো — আমি check করব। Check এ pass হলেই Day 2 পাবে।
> কোনো সমস্যা হলে **আমাকে জিজ্ঞেস করো**, এগিয়ে যেও না।

---

## Lab এর লক্ষ্য

আজকে তুমি নিজের একটা **Personal Introduction Page** তৈরি করবে।
এটা তোমার প্রথম real webpage! 🎉

---

## Step 1: Practice File খোলো

📂 এই path এ যাও: `Day-1/Practice/my-work.html`
এই file এই তোমার সব কাজ করবে।

1. VS Code খোলো
2. এই folder এ যাও: `Web_Development/Phase-1_Foundation/Week-01_HTML5/Day-1/`
3. একটা নতুন file তৈরি করো: `index.html`

---

## Step 2: Basic Structure লেখো

প্রথমে VS Code এ এটা লেখো (copy-paste করো না, নিজে টাইপ করো!):

```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>আমার পরিচয়</title>
</head>
<body>

    <!-- এখানে তোমার content লিখবে -->

</body>
</html>
```

---

## Step 3: Tasks (একটা একটা করো)

### Task 1 — নাম এবং পরিচয় (Beginner)
`<body>` এর ভেতরে লেখো:

```html
<h1>আমার নাম [তোমার নাম]</h1>
<p>আমি [তোমার বয়স] বছর বয়সী।</p>
<p>আমি [তোমার শহর] থেকে।</p>
<p>আমি Full Stack Web Development শিখছি।</p>
```

---

### Task 2 — Bold এবং Italic ব্যবহার করো
```html
<p>আমার <b>পছন্দের বিষয়</b> হলো <i>Technology</i> এবং <i>Programming</i>।</p>
<p>আমার <strong>লক্ষ্য</strong> হলো একজন <em>Professional Developer</em> হওয়া।</p>
```

---

### Task 3 — Section Headings যোগ করো
```html
<h2>আমার সম্পর্কে</h2>
<p>[নিজের সম্পর্কে ৩-৪ লাইন লেখো]</p>

<h2>আমার শখ</h2>
<p>[তোমার শখ লেখো]</p>

<h2>আমার লক্ষ্য</h2>
<p>[তুমি Developer হিসেবে কী করতে চাও তা লেখো]</p>
```

---

### Task 4 — Horizontal Line যোগ করো
```html
<h1>আমার নাম [তোমার নাম]</h1>
<hr>
<p>আমার পরিচয়...</p>
```

---

### Task 5 — Comments যোগ করো
তোমার code এ ৩টি comment যোগ করো। উদাহরণ:
```html
<!-- এটা আমার পরিচয় section -->
<h2>আমার সম্পর্কে</h2>
```

---

## Step 4: Browser এ দেখো

VS Code এ file খোলা রাখো, তারপর:
- **Live Server** দিয়ে চালাও: নিচে `Go Live` button এ click করো
- অথবা file টা Chrome এ drag করে দাও

---

## Step 5: চ্যালেঞ্জ Task (Bonus!)

এগুলো করতে পারলে তুমি এগিয়ে আছো:

```html
<!-- চ্যালেঞ্জ 1: Line break ব্যবহার করো -->
<p>আমার ঠিকানা:<br>বাড়ি নং: ১২৩<br>ঢাকা, বাংলাদেশ</p>

<!-- চ্যালেঞ্জ 2: Underline text -->
<p>আমার <u>favorite quote</u>: "Code করো, স্বপ্ন পূরণ করো।"</p>

<!-- চ্যালেঞ্জ 3: Nested tags -->
<p>আমি <b><i>খুব উত্সাহী</i></b> programmer হতে চাই।</p>
```

---

## ✅ Lab Checklist

Lab শেষ করার আগে নিচের সব check করো:

- [ ] `<!DOCTYPE html>` আছে
- [ ] `<html>`, `<head>`, `<body>` সব ঠিকমতো আছে
- [ ] একটাই `<h1>` আছে
- [ ] কমপক্ষে ২টো `<h2>` আছে
- [ ] কমপক্ষে ৪টো `<p>` আছে
- [ ] `<b>` বা `<strong>` ব্যবহার করেছো
- [ ] `<i>` বা `<em>` ব্যবহার করেছো
- [ ] কমপক্ষে ২টো comment আছে
- [ ] Browser এ ঠিকমতো দেখাচ্ছে

---

## সম্পূর্ণ উদাহরণ (শুধু check করার জন্য, নিজে করার পর দেখো)

```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>রাহুল এর পরিচয়</title>
</head>
<body>

    <!-- Header Section -->
    <h1>আমার নাম রাহুল</h1>
    <hr>

    <!-- About Section -->
    <h2>আমার সম্পর্কে</h2>
    <p>আমি <b>২২ বছর</b> বয়সী। আমি <i>ঢাকা</i> থেকে।</p>
    <p>আমি <strong>Full Stack Developer</strong> হতে চাই।</p>

    <!-- Hobbies Section -->
    <h2>আমার শখ</h2>
    <p>আমার শখ হলো <b>coding</b>, <i>reading</i> এবং <u>gaming</u>।</p>

    <!-- Goals Section -->
    <h2>আমার লক্ষ্য</h2>
    <p>আমার লক্ষ্য হলো <em>AI দিয়ে অসাধারণ web app</em> তৈরি করা।</p>
    <p>আমি প্রতিদিন <b>৩ ঘন্টা</b> অনুশীলন করব।</p>

</body>
</html>
```

---

## 🎉 Lab শেষ? এখন কী করবে?

1. `Practice/my-work.html` file টা Browser এ দেখো — সব ঠিক আছে কিনা
2. নিজে checklist এর সব tick করো
3. আমাকে বলো: **"আমি Day 1 lab শেষ করেছি, check করো"**
4. আমি তোমার কাজ দেখব এবং feedback দেব
5. সব ঠিক থাকলে Day 2 পাবে — না হলে কোথায় ভুল সেটা বলব

**⛔ Day 2 এর material আপাতত নেই — Lab পাস করলে পাবে!**

**কোনো সমস্যা হলে আমাকে জিজ্ঞেস করো** 💬
