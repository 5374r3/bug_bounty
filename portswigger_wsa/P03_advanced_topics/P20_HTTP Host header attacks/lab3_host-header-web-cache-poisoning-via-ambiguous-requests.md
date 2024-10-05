# Web cache poisoning via ambiguous requests

## This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) due to discrepancies in how the cache and the back-end application handle ambiguous requests. An unsuspecting user regularly visits the site's home page.

## To solve the lab, poison the cache so the home page executes `alert(document.cookie)` in the victim's browser

---

### step 1

send homepage into repeter

![screenshot](images/lab3_home_page_repeter.jpg)

### step2

change host name

![screenshot](images/lab3_hostname_change_homepage.jpg)

### step3

add cache buster and use original host name

![screenshot](images/lab3_use_cache_buster_into_repeter.jpg)

### step4

if you add another host
you will get sever error
when x-cache: hit
add another host (see ### step5)

![screenshot](images/lab3_x_cache_hit.jpg)

### step5

add another Host: text.example.com

![screenshot](images/lab3_add_another_host.jpg)

### step6

add payload `alert(document.cookie`

![screenshot](images/lab3_added_payload_into_expolit.jpg)

### step7

replace Host with expolite host

![screenshot](images/lab3_final_payload.jpg)

lab solved

Note:
if you want alert pop up
right click inside repeter and request in browser current session copy url paste into browser

![screenshot](images/lab3_alert_popUp.jpg)
