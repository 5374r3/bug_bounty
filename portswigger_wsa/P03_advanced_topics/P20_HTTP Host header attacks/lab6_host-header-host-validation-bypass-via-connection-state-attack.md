# Host validation bypass via connection state attack

## This lab is vulnerable to routing-based [SSRF](https://portswigger.net/web-security/ssrf) via the Host header. Although the front-end server may initially appear to perform robust validation of the Host header, it makes assumptions about all requests on a connection based on the first request it receives.

## To solve the lab, exploit this behavior to access an internal admin panel located at `192.168.0.1/admin`, then delete the user `carlos`.

---

### step 1

![screenshot](./images/lab6_homepage_repeter.png)

### step2

![screenshot](./images/lab6_admin_page_request.png)

### step3

![screenshot](./images/lab6_get_request_url_with_admin.png)

### step4

![screenshot](./images/lab6_add_csrf_token_and_username.png)

### step5

change request method from get to post

![screenshot](./images/lab6_change_request_method_get_to_post.png)

### step6

remove url
simply test /admin/delete with post request
lab will solve

![screenshot](./images/lab6_remove_url_from_post_request.png)
