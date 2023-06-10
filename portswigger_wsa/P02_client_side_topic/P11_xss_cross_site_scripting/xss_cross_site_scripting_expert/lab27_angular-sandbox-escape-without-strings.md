# Reflected XSS with AngularJS sandbox escape without strings

## This lab uses [AngularJS](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection) in an unusual way where the `$eval` function is not available and you will be unable to use any strings in AngularJS.

## To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that escapes the sandbox and executes the `alert` function without using the `$eval` function.
