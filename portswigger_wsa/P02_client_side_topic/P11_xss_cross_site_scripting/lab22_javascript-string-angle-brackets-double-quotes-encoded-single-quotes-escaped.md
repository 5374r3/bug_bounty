# Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

## This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search query tracking functionality where angle brackets and double are HTML encoded and single quotes are escaped.

## To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the `alert` function.

### HINT: `\'-alert(1)//`

put \'-alert(1)// into seach bar
