# Day 2 — CSS Box Model: Margin, Padding, Border
## 📖 Study Material

---

## 1. CSS Box Model কী?
ওয়েবসাইটে প্রতিটি HTML element (যেমন `<h1>`, `<p>`, `<div>`) আসলে একটা চতুর্ভুজ বাক্সের (Box) মতো। এই বাক্সের চারপাশে স্পেস (ফাঁকা জায়গা) এবং বর্ডার দেওয়ার নিয়মকেই **Box Model** বলে।

Box Model-এর ৪টি অংশ থাকে (ভেতর থেকে বাইরের দিকে):
1. **Content:** আসল কনটেন্ট (যেমন লেখা বা ছবি)।
2. **Padding:** কনটেন্ট এবং বর্ডারের মাঝখানের ফাঁকা জায়গা (ভেতরের ফাঁকা)।
3. **Border:** বাক্সের দেয়াল বা বর্ডার।
4. **Margin:** বর্ডারের বাইরের ফাঁকা জায়গা (এক বাক্স থেকে অন্য বাক্সের দূরত্ব)।

---

## 2. Padding (প্যাডিং)
প্যাডিং মানে হলো বাক্সের ভেতরের স্পেস।

```css
.box {
    /* চারদিকে 20px প্যাডিং */
    padding: 20px; 
    
    /* আলাদা আলাদা দিকে প্যাডিং */
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 10px;
    padding-left: 20px;
    
    /* শর্টকাট (Top-Right-Bottom-Left) বা ঘড়ির কাঁটার নিয়মে */
    padding: 10px 20px 10px 20px; 
    
    /* শর্টকাট (Top/Bottom, Right/Left) */
    padding: 10px 20px; 
}
```

---

## 3. Margin (মার্জিন)
মার্জিন মানে হলো বাক্সের বাইরের স্পেস, যা এটিকে অন্য element থেকে দূরে সরিয়ে দেয়।

```css
.box {
    /* চারদিকে 20px মার্জিন */
    
    margin: 20px; 
    
    /* আলাদা আলাদা দিকে মার্জিন */
    margin-top: 15px;
    margin-bottom: 15px;
    
    /* শর্টকাট (Top/Bottom, Right/Left) */
    margin: 10px 20px; 
    
    /* বাক্সের ডানে-বাঁয়ে সমান মার্জিন দিয়ে মাঝখানে (Center) আনার ম্যাজিক! */
    margin: 0 auto; 
}
```

---

## 4. Border (বর্ডার)
বর্ডার মানে বাক্সের চারপাশের দেয়াল বা দাগ।

```css
.box {
    /* বর্ডার শর্টকাট: (মোটা, স্টাইল, রঙ) */
    border: 2px solid black; 
    
    /* স্টাইলের ধরন: solid (টানা দাগ), dashed (ড্যাশ ড্যাশ), dotted (বিন্দু) */
    border: 3px dashed blue; 

    /* বর্ডারের কোণা গোল (Round) করা */
    border-radius: 10px; 
}
```

---

## 5. Width & Height (প্রস্থ ও উচ্চতা)

```css
.box {
    width: 300px; /* চওড়ায় 300 পিক্সেল */
    height: 200px; /* লম্বায় 200 পিক্সেল */
}
```

---

## 6. একটি Complete Box এর উদাহরণ

```html
<div class="card">
    <h2>Beautiful Card</h2>
    <p>This is a nicely styled card using CSS Box Model.</p>
</div>
```

```css
.card {
    background-color: #ffffff;
    width: 300px;
    padding: 20px;
    margin: 30px auto; /* উপরে-নিচে 30px, ডানে-বাঁয়ে auto (মাঝখানে আসবে) */
    border: 1px solid #ccc; /* হালকা ধূসর বর্ডার */
    border-radius: 10px; /* গোল কোণা */
    text-align: center;
}
```

---

## 7. আজকের Summary

✅ **Padding** = ভেতরের স্পেস।  
✅ **Margin** = বাইরের স্পেস।  
✅ **Border** = দাগ বা সীমানা।  
✅ **border-radius** দিয়ে কোণা গোল করা যায়।  
✅ `margin: 0 auto;` ব্যবহার করে কোনো বাক্সকে পেজের ঠিক মাঝখানে আনা যায়।

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
