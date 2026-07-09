# Day 3 — Tables এবং Forms
## 📖 Study Material

---

## 1. Tables (সারণী)

Table দিয়ে ডেটা সুন্দরভাবে সারিবদ্ধ করে দেখানো যায় (যেমন: রুটিন, রেজাল্ট শিট, বা প্রাইস লিস্ট)।

```html
<table border="1">
    <!-- Table Header (উপরের heading অংশ) -->
    <thead>
        <tr>
            <th>নাম</th>
            <th>বয়স</th>
            <th>শহর</th>
        </tr>
    </thead>
    
    <!-- Table Body (মূল ডেটা) -->
    <tbody>
        <tr>
            <td>সাওন</td>
            <td>২৩</td>
            <td>খুলনা</td>
        </tr>
        <tr>
            <td>রাহুল</td>
            <td>২২</td>
            <td>ঢাকা</td>
        </tr>
    </tbody>
</table>
```

### Table Tags:
| Tag | কাজ |
|-----|-----|
| `<table>` | পুরো table তৈরি করে |
| `<thead>` | Table-এর Header section |
| `<tbody>` | Table-এর Body section |
| `<tr>` | Table Row (সারি) |
| `<th>` | Table Header cell (টেক্সট bold হয়) |
| `<td>` | Table Data cell (সাধারণ ডেটা) |

---

## 2. Forms (ফর্ম)

Form দিয়ে ইউজারের কাছ থেকে ডেটা নেওয়া হয় (যেমন: লগইন, সাইন আপ বা কন্টাক্ট ফর্ম)।

```html
<form action="/submit" method="POST">

    <!-- Text Input (সাধারণ লেখা) -->
    <label for="name">নাম:</label>
    <input type="text" id="name" name="name" placeholder="তোমার নাম লেখো">
    <br><br>

    <!-- Email Input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="email@example.com">
    <br><br>

    <!-- Number Input -->
    <label for="age">বয়স:</label>
    <input type="number" id="age" name="age" min="1" max="100">
    <br><br>

    <!-- Textarea (বড় মেসেজ লেখার জায়গা) -->
    <label for="message">বার্তা:</label>
    <textarea id="message" name="message" rows="4" cols="40"></textarea>
    <br><br>

    <!-- Radio Buttons (যেকোনো একটা বেছে নেওয়া) -->
    <p>লিঙ্গ:</p>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">পুরুষ</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">মহিলা</label>
    <br><br>

    <!-- Checkboxes (একাধিক বেছে নেওয়া) -->
    <p>কী কী শিখতে চাও?</p>
    <input type="checkbox" id="html" name="skills" value="html">
    <label for="html">HTML</label>
    <input type="checkbox" id="css" name="skills" value="css">
    <label for="css">CSS</label>
    <br><br>

    <!-- Select Dropdown (লিস্ট থেকে বেছে নেওয়া) -->
    <label for="city">শহর:</label>
    <select id="city" name="city">
        <option value="">-- শহর বেছে নাও --</option>
        <option value="khulna">খুলনা</option>
        <option value="dhaka">ঢাকা</option>
    </select>
    <br><br>

    <!-- Submit Button -->
    <button type="submit">Submit করো</button>

</form>
```

---

## 3. Important Attributes in Forms

| Attribute | কাজ |
|-----------|-----|
| `id` ও `for`| `label` এর `for` এবং `input` এর `id` এক হতে হবে, যাতে ক্লিক করলে কানেক্ট হয়। |
| `placeholder` | ইনপুট বক্সে হালকা করে hint লেখা থাকে। |
| `required` | এটা দিলে ইউজার ঐ ঘরটা পূরণ না করে ফর্ম সাবমিট করতে পারবে না। |
| `name` | সার্ভারে ডেটা পাঠানোর সময় এই নাম ধরে যায় (ব্যাকএন্ডের জন্য জরুরি)। |

---

## 4. আজকের Summary

✅ `<table>` দিয়ে সুন্দর structured ডেটা দেখানো যায়।  
✅ `<form>` দিয়ে ইউজারের input নেওয়া যায়।  
✅ `<label>` সবসময় `<input>` এর সাথে থাকা উচিত।  

---

## পরের ধাপ
✅ এই material পড়া শেষ হলে → **[LAB.md](./LAB.md) এ যাও** এবং আজকের Practice শুরু করো!
