# Day 1 — CSS Basics: Selectors, Colors, Fonts
## 📖 Study Material

---

## 1. CSS কী?
**CSS** মানে Cascading Style Sheets। 
HTML যদি একটা বাড়ির কঙ্কাল বা ইট-সিমেন্ট হয়, তবে CSS হলো সেই বাড়ির রঙ, ডিজাইন এবং সাজসজ্জা। CSS ছাড়া কোনো ওয়েবসাইট সুন্দর দেখায় না।

---

## 2. CSS লেখার ৩টি নিয়ম (Ways to include CSS)

**১. Inline CSS (একদম ট্যাগের ভেতরে):**
```html
<p style="color: red; font-size: 20px;">এই লেখাটা লাল হবে</p>
```
*এটা সাধারণত ব্যবহার করা উচিত নয়, কারণ এতে কোড নোংরা হয়ে যায়।*

**২. Internal CSS (`<head>` এর ভেতর `<style>` ট্যাগ দিয়ে):**
```html
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
```

**৩. External CSS (আলাদা ফাইলে):**
সবচেয়ে ভালো নিয়ম! `style.css` নামে একটা আলাদা ফাইল বানিয়ে HTML এর `<head>` এ লিংক করে দিতে হয়:
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

---

## 3. CSS Syntax (লেখার নিয়ম)

```css
selector {
    property: value;
    property: value;
}
```
যেমন:
```css
h1 {
    color: red;
    font-size: 30px;
}
```

---

## 4. CSS Selectors (HTML কে ধরার উপায়)

**১. Element Selector (ট্যাগের নাম দিয়ে):**
```css
p {
    color: green; /* সব <p> সবুজ হয়ে যাবে */
}
```

**২. Class Selector (`.` দিয়ে শুরু হয়):**
HTML: `<h2 class="title">হেডিং</h2>`
CSS:
```css
.title {
    color: blue; /* শুধু title ক্লাসগুলো নীল হবে */
}
```
*(একটি ক্লাস পেজের অনেক জায়গায় ব্যবহার করা যায়)*

**৩. ID Selector (`#` দিয়ে শুরু হয়):**
HTML: `<h2 id="main-title">মেইন হেডিং</h2>`
CSS:
```css
#main-title {
    color: red; /* শুধু এই নির্দিষ্ট আইডিটা লাল হবে */
}
```
*(একটি আইডি পুরো পেজে একবারই ব্যবহার করা উচিত)*

---

## 5. Colors (রঙ)

CSS এ রঙ ৩ ভাবে দেওয়া যায়:
1. **নাম দিয়ে:** `color: red;`, `color: blue;`
2. **HEX Code:** `color: #ff0000;` (ওয়েব ডিজাইনে সবচেয়ে বেশি ব্যবহার হয়)
3. **RGB:** `color: rgb(255, 0, 0);`

```css
body {
    background-color: #f4f4f4; /* পেজের ব্যাকগ্রাউন্ড কালার */
}

h1 {
    color: #333333; /* টেক্সটের কালার */
}
```

---

## 6. Fonts & Text Formatting

```css
p {
    font-size: 18px; /* লেখার সাইজ */
    font-family: Arial, sans-serif; /* ফন্টের স্টাইল */
    font-weight: bold; /* লেখাকে মোটা করার জন্য */
    text-align: center; /* লেখাকে মাঝে আনার জন্য (left, right, center) */
    text-decoration: underline; /* আন্ডারলাইন দেওয়ার জন্য */
    line-height: 1.5; /* দুই লাইনের মাঝের ফাঁকা জায়গা */
}
```

---

## 7. আজকের Summary

✅ External CSS (`link` ট্যাগ) ব্যবহার করা সবচেয়ে ভালো।  
✅ `Class` সিলেক্ট করতে `.` (ডট) ব্যবহার করা হয়।  
✅ `ID` সিলেক্ট করতে `#` (হ্যাশ) ব্যবহার করা হয়।  
✅ `color` মানে টেক্সটের রঙ, আর `background-color` মানে পিছনের রঙ।

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
