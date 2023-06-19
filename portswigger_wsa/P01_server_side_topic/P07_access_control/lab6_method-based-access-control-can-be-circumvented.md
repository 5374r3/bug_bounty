# Method-based access control can be circumvented

## This lab implements [access controls]

based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

## To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed access controls to promote yourself to become an administrator.

NOTE: this lab is solved using two browser with burpsuite enable or use incongnito with burpsuite

---

### step 1

on normal browser login as administrator
make admin to carlos and intercept while making admin
observe the session

### step2

on incognito mode login as wiener
reaload page and intercept the home page after login
send the request to repeter and not down the session id

### step3

on normal browser administraor account
make carlos admin again and intercept
replace the session with wiener session
you will get un-authorise
now make make carlos admin and intercept
this time change post request to POSTX
and change session id with wiener session
forward request you wll get missing usenname or missing on browser

### step4

on normal browser administrator account
make carlos admin again and intercept the request
change session id with wiener session id
and right click on burpsuite change request method
earlier it show
(POST /admin-roles HTTP/1.1)
after change request method
(GET /admin-roles?username=carlos&action=upgrade HTTP/1.1)
change carlos with wiener
(GET /admin-roles?username=wiener&action=upgrade HTTP/1.1)
send forword
lab solve
