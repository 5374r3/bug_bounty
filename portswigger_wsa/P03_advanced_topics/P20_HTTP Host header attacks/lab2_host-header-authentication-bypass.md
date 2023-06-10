# Host header authentication bypass

## This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

## To solve the lab, access the admin panel and delete Carlos's account

### step1

send homepage into repeter

![screenshot](./images/lab2_homepage_into_repeter.png)

### step2

remove host url with any random name
and send request

![screenshot](./images/lab2_homepage_with_random_host.png)

### step3

look for robots.txt page

![screenshot](./images/lab2_robots_txt_file.png)

### step4

try to access admin page

![screenshot](./images/lab2_admin_page.png)

### step5

try to access admin page into repeter

![screenshot](./images/lab2_admin_access_into_repeter.png)

![screenshot](./images/lab2_admin_page_access_by_localhost.png)

### step6

right click and request in browser

![screenshot](./images/portswigger_wsa/P03_advanced_topics/P20_HTTP Host header attacks/images/lab2_admin_panel.png)

### step7

delete carlos account
but you cannot delete

![screenshot](./images/lab2_delete_carlos_account.png)

### step8

add _/admin/delete?username=carlos_
into repeter
and send request
carlos account will be deleted

![screenshot](./images/lab2_carlos_account_deleted.png)
