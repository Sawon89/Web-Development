# HTML5 Quick Reference — Cheat Sheet
## সব গুরুত্বপূর্ণ HTML tags এক জায়গায়

---

## Document Structure
```html
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Page description">
    <title>Page Title</title>
</head>
<body>
    <!-- Content -->
</body>
</html>
```

---

## Semantic Layout Tags
```html
<header>    — উপরের অংশ (logo, nav)
<nav>       — Navigation menu
<main>      — মূল content
<section>   — Thematic section
<article>   — Standalone content
<aside>     — Sidebar content
<footer>    — নিচের অংশ
```

---

## Text Tags
```html
<h1> থেকে <h6>    — Headings
<p>               — Paragraph
<b>               — Bold (visual)
<strong>          — Bold (important)
<i>               — Italic (visual)
<em>              — Italic (emphasized)
<u>               — Underline
<mark>            — Highlight
<small>           — Small text
<del>             — Strikethrough
<sup>             — Superscript: x²
<sub>             — Subscript: H₂O
<br>              — Line break
<hr>              — Horizontal rule
```

---

## Lists
```html
<!-- Unordered -->
<ul>
    <li>Item</li>
</ul>

<!-- Ordered -->
<ol>
    <li>Item</li>
</ol>

<!-- Description -->
<dl>
    <dt>Term</dt>
    <dd>Definition</dd>
</dl>
```

---

## Links
```html
<a href="url">Text</a>
<a href="url" target="_blank">New tab</a>
<a href="#section-id">Same page</a>
<a href="mailto:email@x.com">Email</a>
<a href="tel:+8801700000000">Phone</a>
```

---

## Images
```html
<img src="path" alt="description" width="300">

<figure>
    <img src="path" alt="description">
    <figcaption>Caption</figcaption>
</figure>
```

---

## Tables
```html
<table>
    <thead>
        <tr>
            <th>Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>Footer</td>
        </tr>
    </tfoot>
</table>
```

---

## Forms
```html
<form action="/submit" method="POST">

    <label for="id">Label</label>
    <input type="text" id="id" name="name" required>

    <input type="email">      — Email
    <input type="password">   — Password
    <input type="number">     — Number
    <input type="tel">        — Phone
    <input type="date">       — Date
    <input type="checkbox">   — Checkbox
    <input type="radio">      — Radio
    <input type="file">       — File upload
    <input type="hidden">     — Hidden field

    <textarea rows="4"></textarea>

    <select>
        <option value="val">Text</option>
    </select>

    <button type="submit">Submit</button>
    <button type="reset">Reset</button>

</form>
```

---

## Special Characters
```html
&copy;   → ©
&amp;    → &
&lt;     → <
&gt;     → >
&nbsp;   → (non-breaking space)
&bull;   → •
&mdash;  → —
```

---

## Useful ARIA
```html
aria-label="description"
aria-describedby="element-id"
aria-required="true"
aria-hidden="true"
role="alert"
role="button"
tabindex="0"
```

---

*এই cheat sheet টা সবসময় কাছে রাখো!* 📌
