# Reflected XSS protected by very strict CSP, with dangling markup attack

## This lab using a strict [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy) that blocks outgoing requests to external web sites.

## To solve the lab, first perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that bypasses the CSP and exfiltrates a simulated victim user's [CSRF](https://portswigger.net/web-security/csrf) token using Burp Collaborator. You then need to change the simulated user's email address to `hacker@evil-user.net`.

## You must label your vector with the word "Click" in order to induce the simulated user to click it. For example:

## `<a href="">Click me</a>`
