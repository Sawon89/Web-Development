# Day 3 — CSS Flexbox (1D Layout)
## 📖 Study Material

---

## 1. Flexbox কী?
আগে ওয়েবসাইট লেআউট (Layout) তৈরি করা খুব কঠিন ছিল, কিন্তু **Flexbox (Flexible Box)** আসার পর তা একদম সহজ হয়ে গেছে।
Flexbox দিয়ে যেকোনো এলিমেন্টকে (Element) খুব সহজে পাশাপাশি বা উপরে-নিচে সাজানো যায়। এটা একটা **1-Dimensional** (একমাত্রিক) লেআউট সিস্টেম, অর্থাৎ এটা হয় ডানে-বামে কাজ করে, না হয় উপরে-নিচে কাজ করে।

---

## 2. Flexbox-এর বেসিক ধারণা
Flexbox ব্যবহার করতে হলে তোমাকে একটা Parent Element (যেমন একটা <div>) কে "Flex Container" বানাতে হবে। তার ভেতরের জিনিসগুলো তখন "Flex Items" হয়ে যাবে।

```css
/* Container কে Flexbox বানানোর ম্যাজিক */
.container {
    display: flex;
}
```
**যেই `display: flex;` দিবে, ভেতরের আইটেমগুলো অটোমেটিক পাশাপাশি (Row-তে) বসে যাবে!**

---

## 3. Flex Direction (দিক পরিবর্তন করা)
তুমি চাইলে আইটেমগুলো পাশাপাশি বা নিচে-নিচে সাজাতে পারো।

```css
.container {
    display: flex;
    flex-direction: row; /* ডিফল্ট: পাশাপাশি বসে (বাম থেকে ডানে) */
    /* flex-direction: column; /* উপরে-নিচে বসে */
    /* flex-direction: row-reverse; /* ডান থেকে বামে বসে */
}
```

---

## 4. Justify Content (ডানে-বামে সরানো)
আইটেমগুলোকে ডানে, বামে বা মাঝখানে সাজানোর জন্য `justify-content` ব্যবহার করা হয়।
*(এটা Main Axis বরাবর কাজ করে)*

```css
.container {
    display: flex;
    justify-content: flex-start; /* বামে (ডিফল্ট) */
    /* justify-content: flex-end; /* ডানে */
    /* justify-content: center; /* একদম মাঝখানে */
    /* justify-content: space-between; /* প্রথমটা বামে, শেষটা ডানে, বাকিগুলো মাঝে সমান ফাঁকা */
    /* justify-content: space-around; /* সবগুলোর চারপাশে সমান ফাঁকা */
}
```

---

## 5. Align Items (উপরে-নিচে সরানো)
আইটেমগুলোকে উপরে, নিচে বা মাঝখানে সাজানোর জন্য `align-items` ব্যবহার করা হয়।
*(এটা Cross Axis বরাবর কাজ করে)*

```css
.container {
    display: flex;
    height: 300px; /* উচ্চতা না থাকলে বুঝতে পারবে না */
    align-items: stretch; /* টেনে লম্বা করে দেয় (ডিফল্ট) */
    /* align-items: flex-start; /* উপরে */
    /* align-items: flex-end; /* নিচে */
    /* align-items: center; /* উপরে-নিচে একদম মাঝখানে (খুব দরকারি!) */
}
```

---

## 6. একটি বস্তুকে একদম ঠিক মাঝখানে (Perfect Center) আনার জাদুকরী কোড!

এই কোডটা সারা জীবন কাজে লাগবে:

```css
.center-div {
    display: flex;
    justify-content: center; /* ডানে-বামে মাঝে আনবে */
    align-items: center; /* উপরে-নিচে মাঝে আনবে */
    height: 100vh; /* পুরো স্ক্রিনের সমান উচ্চতা */
}
```

---

## 7. Flex Wrap (লাইন ভেঙে নিচে নামা)
যদি তোমার অনেকগুলো আইটেম থাকে এবং স্ক্রিনে জায়গা না ধরে, তবে ডিফল্টভাবে সেগুলো কুঁচকে যায়। `flex-wrap: wrap;` দিলে সেগুলো জায়গা না পেলে পরের লাইনে চলে আসবে।

```css
.container {
    display: flex;
    flex-wrap: wrap; 
}
```

---

## 8. আজকের Summary

✅ **`display: flex;`** দিয়ে Flexbox চালু করতে হয়।  
✅ **`flex-direction`** দিয়ে সারি (row) বা কলাম (column) ঠিক করা যায়।  
✅ **`justify-content`** দিয়ে ডানে-বামে (Main Axis) সাজানো যায়।  
✅ **`align-items`** দিয়ে উপরে-নিচে (Cross Axis) সাজানো যায়।

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
