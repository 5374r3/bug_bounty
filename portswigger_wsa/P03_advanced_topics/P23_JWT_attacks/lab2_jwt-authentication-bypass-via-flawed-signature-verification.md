lab

# JWT authentication bypass via flawed signature verification

## This lab uses a JWT-based mechanism for handling sessions. The server is insecurely configured to accept unsigned JWTs.

## To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

---

step 1

login to account send /my-account to repeater

![[lab2_my_account_jwt_token.png]]

![[lab2_jws_wiener_account.png]]

step 2
use user administrator in sub send request
you will get 302 found which is successful
but location /login

![[lab2_aministrator_302_but_not_login.png]]

step 3
use sub as administrator
Alg:none
send request

![[lab2_alg_non_sub_aministrator.png]]

![[lab2_my_account_request_with_modified_token.png]]

step 4

now change to /admin and send request

![[lab2_aministrator_alg_none.png]]

![[lab2_get_admin_request.png]]

make sure alg : none

![[lab2_alog_non_administrator.png]]

step 5
send GET /admin/delete?username=carlos

![[portswigger_wsa/P03_advanced_topics/P23_JWT_attacks/images/lab2_delete_carlos_account.png]]

![[portswigger_wsa/P03_advanced_topics/P23_JWT_attacks/images/lab2_solved_lab.png]]
