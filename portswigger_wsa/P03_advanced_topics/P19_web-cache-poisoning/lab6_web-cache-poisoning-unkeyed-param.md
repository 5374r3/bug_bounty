# Web cache poisoning via an unkeyed query parameter

## This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) because it excludes a certain parameter from the cache key. A user regularly visits this site's home page using Chrome.

## To solve the lab, poison the cache with a response that executes `alert(1)` in the victim's browser.

---

### step 1

send homepage to the repeter

![screenshot](./images/lab6_homepage_into_repeter.png)

### step2

add cache buster
/?test=124 (it can be anything)

![screenshot](./images/lab6_added_cache_buster_to_homepage.png)

### step3

Note: when age: > 0 and x-cache:hit
send param miner (header => guess GET parameter)
and again send request into repeter

![screenshot](./images/lab6_param_miner_output_homepage.png)

### step4

added _/?test=124&utm_content=zwrtxqvaltp0fwtqx8&xomohdiqmx6=1&vrnn08k41=1_

![screenshot](./images/lab6_add_utm_content_into_repeter.png)

### step5

testing hello

![screenshot](./images/lab6_testing_hello_with_cache_buster.png)

### step6

open current session into browser

![screenshot](./images/lab6_home_page_with_hello.png)

### step7

final payload
_/?utm_content='/><script>alert(1)</script>_

![screenshot](./images/lab6_final_payload_utm_alert.png)

### step8

\
lab solved message will appear
still to confirm pop up
request current session into browser
reload page many times pop up will appear

![screenshot](./images/lab6_popup_mesage_testing_payload.png)
