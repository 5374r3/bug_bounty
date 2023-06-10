# Web cache poisoning with an unkeyed header

## This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) because it handles input from an unkeyed header in an unsafe way. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

### step1

![screenshot](./images/lab1_send_homepage_to_repeter.png)

### step2

add _X-forword-Host : any url without https or http_

![screenshot](./images/lab1_x_forword_host_x-cache.png)

### step3

inspect resourcee file
![screenshot](./images/lab1_tracking_js_file.png)

### step4

add payload to the resource/js/tracking.js

![screenshot](./images/lab1_expolite_alert_payload.png)

### step5

![screenshot](./images/lab1_x-forword_host_repeter.png)

### step6

reload page alert will pop up lab solve
![screenshot](./images/lab1_alert_pop_up.png)
