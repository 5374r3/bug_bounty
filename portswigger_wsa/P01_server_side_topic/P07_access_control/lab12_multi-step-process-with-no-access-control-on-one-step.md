# Multi-### stepprocess with no access control on one step

## This lab has an admin panel with a flawed multi-### stepprocess for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

## To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed [access controls] to promote yourself to become an administrator.

we need incognito mode and normal mode for two different session

---

### step 1

login normal window wiener accout
note down session id or sent to repeater

### step2

login as administrater
not down sesson id or sent to repeater

### step3

go to admin panel
upgrade carlos account and intercept
action=upgrade&username=carlos
on browser you will notice go back or yes two button available to confirm
click yes and watch on intercept page
action=upgrade&confirmed=true&username=carlos

### step4

perform 3 ### stepwith wiener
copy administrator sesson id and paste to wiener session id
now wiener get admin panel click on admin panel not authoried
so intercept admin panel
and again chages session id of wiener with administrator id
click on wiener and upgrade see and watch on intercept
action=upgrade&username=wiener
now
add &confirmed=true
action=upgrade&confirmed=true&username=wiener
and forword request
lab solved
