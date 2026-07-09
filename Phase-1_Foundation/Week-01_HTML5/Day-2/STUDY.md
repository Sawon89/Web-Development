# Day 2 — Links, Lists এবং Images
## 📖 Study Material

---

## 1. Links — `<a>` Tag

Link দিয়ে এক page থেকে আরেক page এ যাওয়া যায়। HTML এ link তৈরি করতে `<a>` (anchor) tag ব্যবহার করা হয়।

```html
<!-- বাইরের website এ link -->
<a href="https://www.google.com">Google এ যাও</a>

<!-- নতুন tab এ খুলবে (target="_blank") -->
<a href="https://www.github.com" target="_blank">GitHub</a>

<!-- একই page এর অন্য section এ (id দিয়ে) -->
<a href="#about">আমার সম্পর্কে দেখো</a>

<!-- Email link (mailto) -->
<a href="mailto:example@email.com">আমাকে email করো</a>

<!-- Phone link (tel) -->
<a href="tel:+8801700000000">ফোন করো</a>
```

### Important attribute:
- `href` = Link এর ঠিকানা (কোথায় যাবে)

---

## 2. Lists (তালিকা)

### Unordered List (bullet points - `<ul>`):
কোনো ক্রম বা sequence না থাকলে এটা ব্যবহার করা হয়।
```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

### Ordered List (numbered - `<ol>`):
ক্রম বা sequence থাকলে এটা ব্যবহার করা হয় (যেমন: ১, ২, ৩)।
```html
<ol>
    <li>প্রথমে HTML শিখবো</li>
    <li>তারপর CSS</li>
    <li>তারপর JavaScript</li>
</ol>
```

### Nested List (list এর ভেতরে list):
```html
<ul>
    <li>Frontend
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>
    <li>Backend
        <ul>
            <li>Node.js</li>
            <li>Express.js</li>
        </ul>
    </li>
</ul>
```

---

## 3. Images — `<img>` Tag

ছবি দেখানোর জন্য `<img>` tag ব্যবহার করা হয়। এটা একটা self-closing tag।

```html
<!-- Online image -->
<img src="https://picsum.photos/300/200" alt="Random photo">

<!-- Local image (তোমার folder এ থাকা ছবি) -->
<img src="photo.jpg" alt="আমার ছবি">

<!-- Width এবং Height দিয়ে (optional) -->
<img src="photo.jpg" alt="ছবি" width="300" height="200">
```

### Important attributes:
- `src` = ছবির path বা URL (কোথায় ছবিটা আছে)
- `alt` = ছবি না দেখালে বা screen reader এর জন্য যা দেখাবে (accessibility এর জন্য **অবশ্যই** দিতে হবে!)
- `width` / `height` = ছবির size

---

## 4. আজকের Summary

✅ `<a href="">` — links তৈরি করে  
✅ `target="_blank"` — link নতুন tab এ খোলে  
✅ `<ul>` — bullet list  
✅ `<ol>` — numbered list  
✅ `<li>` — list item (ul বা ol এর ভেতরে থাকে)  
✅ `<img src="" alt="">` — images দেখায়  

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
