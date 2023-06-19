# Web cache poisoning via an unkeyed query string

## This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) because the query string is unkeyed. A user regularly visits this site's home page using Chrome.

## To solve the lab, poison the home page with a response that executes `alert(1)` in the victim's browser.

---

### step 1

send home page into repeter and send request
the value of age will change at each request and x-cache: hit
once value of age = 0
x-cache: miss

![screenshot](./images/lab5_homepage_into_repeter.png)

### step2

add cache-buster query parameter eg /?cb=1222
so /?test=123

![screenshot](./images/lab5_add_test_as_cache_buster.png)

### step3

![screenshot](./images/lab5_test_another_cache_buster_with_quotes.png)

### step4

right click request on browser current session

![screenshot](./images/lab5_current_seeion_in_browser_with_hello.png)

### step5

note:
max-age = 35
age:31
x-cache: hit
it will not store payload untill age=0 and x-cache: miss
![screenshot](./images/lab5_payload_testing.png)

### step6

![screenshot](./images/lab5_payload_request_final.png)

### step7

lab will solve after request
still right click over repeter
go to request in browser
go to current session copy url paste into browser
lab solved

![screenshot](./images/lab5_alert_pop_up.png)
