# Routing-based SSRF

## This lab is vulnerable to routing-based [SSRF](https://portswigger.net/web-security/ssrf) via the Host header. You can exploit this to access an insecure intranet admin panel located on an internal IP address.

## To solve the lab, access the internal admin panel located in the `192.168.0.0/24` range, then delete Carlos.

### Note: Burp collaborator used so Burpsuite Pro will used to solved the lab

---

### step 1

send Homepage(/) to the repeter

![screenshot](./images/lab4_homePage_into-repeter.png)

### step2

go to burp collaborator
copy to clipboad
replace with host url
`Host: mh7ba0stpilluj3j7qcr4o5b026tuji8.oastify.com`
send request into repeter and go collaborator click on poll now

![screenshot](./images/lab4_burp_collaborator_poll_now.png)

go to repeter after poll now from burp collaborator

![screenshot](./images/lab4_burp_collaborator.png)

### step3

access the internal admin panel located in the `192.168.0.0/24`

![screenshot](./images/lab4_change_host_to_admin_url.png)

### step4

send ( ### step3) to intruder
and uncheck update host header
payload
values:
`From: 0 To: 255 Step: 1`

![screenshot](./images/lab4_payload_mark_uncheck.png)

payload result

![screenshot](./images/lab4_payload_result_admin_url.png)

![screenshot](./images/lab4_payload_result.png)

### step5

![screenshot](./images/lab4_access_admin_page.png)

### step6

add host `Host: 192.168.0.217` from ### step5

![screenshot](./images/lab4_testing_admin_with_admin_host.png)

### step7

from ### step6 request in browser current session

![screenshot](./images/lab4_test_admin_page_into_browser.png)

### step8

it will not work

![screenshot](./images/lab4_delete_user_not_found.png)

### step9

inspect ### step7

![screenshot](./images/lab4_inspect_admin_page_for_csrf.png)

---

### step 10

add _GET /admin/delete?csrf=engoKCu9WKZE7R4XsgDJxYzbkhNJMD8E&username=carlos_

![screenshot](./images/lab4_final_payload_with_csrf_and_username.png)

reload page lab solved

![screenshot](./images/lab4_congratulations_page.png)
