# Day 5 — HTML Accessibility + Best Practices
## 📖 Study Material

---

## 1. Accessibility (প্রবেশযোগ্যতা) কী?

Accessibility মানে হলো—তোমার ওয়েবসাইট যেন **সব ধরনের মানুষ** ব্যবহার করতে পারে। 
যাদের চোখের সমস্যা আছে, তারা সাধারণ স্ক্রিন দেখতে পায় না। তারা "Screen Reader" নামের একটি সফটওয়্যার ব্যবহার করে, যা স্ক্রিনে কী লেখা আছে তা পড়ে শোনায়। তোমার ওয়েবসাইটের কোড যদি সঠিক না হয়, তবে স্ক্রিন রিডার তা ঠিকমতো পড়তে পারবে না। 

এছাড়া যারা মাউস ব্যবহার করতে পারে না, তারা কীবোর্ডের (Tab key) সাহায্যে ওয়েবসাইট ব্রাউজ করে।

---

## 2. ARIA Attributes (Accessibility এর জন্য বিশেষ কোড)

**ARIA** (Accessible Rich Internet Applications) হলো কিছু বিশেষ attribute, যা স্ক্রিন রিডারকে বুঝতে সাহায্য করে।

```html
<!-- aria-label: স্ক্রিন রিডারকে বলে দেয় বাটনটার কাজ কী (যেখানে শুধু আইকন থাকে) -->
<button aria-label="Menu বন্ধ করো">✕</button>

<!-- aria-hidden: স্ক্রিন রিডারকে এটা পড়তে নিষেধ করে (যেমন সাজানোর জন্য ব্যবহৃত আইকন) -->
<span aria-hidden="true">🎉</span> সফল হয়েছে!
```

---

## 3. Keyboard Navigation

সবকিছু কীবোর্ড (Tab) দিয়ে যেন সিলেক্ট করা যায়, সেটা নিশ্চিত করতে হয়।
`<a>`, `<button>`, `<input>` এগুলোতে এমনিতেই Tab কাজ করে। কিন্তু সাধারণ `<div>` বা `<span>`-এ Tab কাজ করাতে চাইলে `tabindex` ব্যবহার করতে হয়।

```html
<!-- tabindex="0" দিলে সাধারণ লেখাও কীবোর্ড দিয়ে সিলেক্ট করা যাবে -->
<div tabindex="0">এই div এ কীবোর্ড দিয়ে focus করা যাবে</div>
```

---

## 4. Images এর Accessibility

ছবিতে `alt` text দেওয়া খুবই জরুরি!
```html
<!-- ✅ ভালো: স্ক্রিন রিডার "Company Logo" পড়ে শোনাবে -->
<img src="logo.png" alt="Company Logo">

<!-- ⚠️ Decorative image (শুধু সাজানোর জন্য, কোনো দরকারি তথ্য নেই) -->
<img src="decoration.png" alt="" role="presentation">
```

---

## 5. Forms এর Accessibility

ফর্মের ইনপুটের সাথে সবসময় `<label>` কানেক্ট করে দিতে হয়।
```html
<!-- সবসময় label এর for এবং input এর id এক হতে হবে -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email" required>
```

---

## 6. HTML Best Practices (ভালো কোড লেখার নিয়ম) চেকলিস্ট

একজন ভালো ডেভেলপার সবসময় নিচের নিয়মগুলো মেনে কোড করেন:

1. **DOCTYPE সবসময় প্রথমে:** `<!DOCTYPE html>`
2. **Language Attribute:** `<html lang="en">` (বা বাংলা হলে "bn")
3. **Meta charset এবং viewport:** মোবাইল রেসপন্সিভ এবং সব ভাষার অক্ষর সাপোর্ট করার জন্য।
4. **Descriptive title:** `<title>` এ সুন্দর ও অর্থবোধক নাম দেওয়া।
5. **একটাই h1:** একটা পেজে শুধু একটাই `<h1>` থাকবে, বাকিগুলো `<h2>`, `<h3>` হবে।
6. **Alt text:** সব ছবিতে `alt` text থাকতে হবে।
7. **Semantic tags:** `<div>` এর বদলে `<header>`, `<main>`, `<footer>` ব্যবহার করা।
8. **Lowercase tags:** সব ট্যাগ ছোট হাতের অক্ষরে লেখা (যেমন `<P>` না লিখে `<p>` লেখা)।

---

## 7. HTML Validation

তোমার HTML কোডে কোনো ভুল আছে কিনা, তা চেক করার জন্য W3C এর একটি টুল আছে। তুমি তোমার কোড সেখানে দিয়ে চেক করে দেখতে পারো যে কোডটি 100% সঠিক কিনা।
🌐 **W3C Validator:** https://validator.w3.org/

---

## Summary

✅ Accessibility সবার জন্য ওয়েবসাইট ব্যবহারযোগ্য করে।  
✅ `alt` text সব ছবিতে দিতেই হবে।  
✅ `label` সব ইনপুটের সাথে লিংক করতে হবে।  
✅ Semantic tags ব্যবহার করতে হবে।  
✅ Heading hierarchy মানতে হবে (h1 → h2 → h3)।  

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
