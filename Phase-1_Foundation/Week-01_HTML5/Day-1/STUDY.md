# Day 1 — HTML কী এবং কীভাবে কাজ করে?
## 📖 Study Material

---

## 1. HTML কী?

**HTML** = **H**yper**T**ext **M**arkup **L**anguage

HTML হলো একটি webpage এর **কাঙ্কাল** (skeleton)। এটা browser কে বলে দেয় — কোথায় কী দেখাতে হবে।

```
ভাবো একটা মানুষের শরীরের মতো:
- HTML = হাড় (structure)
- CSS = কাপড়/চেহারা (style)
- JavaScript = নড়াচড়া (behavior)
```

---

## 2. HTML Document এর Basic Structure

প্রতিটি HTML file এ এই structure থাকে:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>আমার প্রথম Webpage</title>
</head>
<body>
    <!-- এখানে সব content থাকবে -->
    <h1>নমস্কার, আমি শিখছি!</h1>
    <p>এটা আমার প্রথম webpage।</p>
</body>
</html>
```

### প্রতিটি অংশের মানে:

| অংশ | কাজ |
|-----|-----|
| `<!DOCTYPE html>` | Browser কে বলে — এটা HTML5 |
| `<html>` | পুরো document এর শুরু |
| `<head>` | Page এর information (দেখা যায় না) |
| `<meta charset>` | বাংলা/English সব character support করে |
| `<title>` | Browser tab এ যা দেখায় |
| `<body>` | যা screen এ দেখা যায় |

---

## 3. Tags কী?

HTML এ সব কিছু **tags** দিয়ে লেখা হয়।

```html
<tagname>Content</tagname>
```

- **Opening tag:** `<tagname>`
- **Closing tag:** `</tagname>`
- **Content:** মাঝখানে যা লেখা হয়

### উদাহরণ:
```html
<h1>এটা একটা Heading</h1>
<p>এটা একটা Paragraph</p>
<b>এটা Bold text</b>
<i>এটা Italic text</i>
```

### Self-closing Tags (closing tag নেই):
```html
<br>          <!-- Line break -->
<hr>          <!-- Horizontal line -->
<img src="photo.jpg" alt="ছবি">
<input type="text">
```

---

## 4. Headings (শিরোনাম)

HTML এ ৬ ধরনের heading আছে:

```html
<h1>সবচেয়ে বড় Heading — শুধু একটা page এ</h1>
<h2>দ্বিতীয় বড়</h2>
<h3>তৃতীয়</h3>
<h4>চতুর্থ</h4>
<h5>পঞ্চম</h5>
<h6>সবচেয়ে ছোট</h6>
```

> ⚠️ **Important:** প্রতিটি page এ শুধু **একটি** `<h1>` ব্যবহার করবে। এটা SEO এর জন্য গুরুত্বপূর্ণ।

---

## 5. Paragraphs এবং Text Formatting

```html
<p>এটা একটা paragraph।</p>

<p>এই text এ <b>bold</b> আছে।</p>
<p>এই text এ <i>italic</i> আছে।</p>
<p>এই text এ <u>underline</u> আছে।</p>
<p>এই text এ <strong>important bold</strong> আছে।</p>
<p>এই text এ <em>emphasized italic</em> আছে।</p>

<!-- Line break -->
<p>প্রথম লাইন<br>দ্বিতীয় লাইন</p>
```

---

## 6. HTML Attributes

Tags এর ভেতরে extra information দেওয়া হয় **attributes** দিয়ে:

```html
<tagname attribute="value">Content</tagname>
```

### উদাহরণ:
```html
<!-- id attribute — unique identifier -->
<h1 id="main-title">আমার পেজ</h1>

<!-- class attribute — grouping -->
<p class="intro-text">পরিচিতি</p>

<!-- lang attribute -->
<html lang="bn">
```

---

## 7. Comments

Code এ note লেখার জন্য comments ব্যবহার করো। Browser এ দেখা যায় না:

```html
<!-- এটা একটা comment — browser এ দেখা যাবে না -->
<p>এটা দেখা যাবে</p>
```

---

## 8. আজকের মূল বিষয়গুলো (Summary)

✅ HTML হলো webpage এর structure  
✅ Tags দিয়ে content define করা হয়  
✅ Opening + Closing tag মিলে একটা element  
✅ Attributes tags এ extra information দেয়  
✅ h1 থেকে h6 headings, p paragraph  
✅ প্রতিটি page এ শুধু একটা h1  

---

## 9. অতিরিক্ত Resources

- 📺 [MDN Web Docs — HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- 📺 [W3Schools HTML Tutorial](https://www.w3schools.com/html/)

---

## পরের ধাপ

✅ এই material পড়া শেষ হলে → **[Lab এ যাও](./LAB.md)**
