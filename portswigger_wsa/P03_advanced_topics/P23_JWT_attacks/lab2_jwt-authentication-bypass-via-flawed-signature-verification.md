# JWT authentication bypass via flawed signature verification

## This lab uses a JWT-based mechanism for handling sessions. The server is insecurely configured to accept unsigned JWTs.

## To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

---

step 1

login to account send /my-account to repeater

![](images/lab2_my_account_jwt_token.jpg)

![](images/lab2_jws_wiener_account.jpg)

step 2
use user administrator in sub send request
you will get 302 found which is successful
but location /login

![](images/lab2_aministrator_302_but_not_login.jpg)

step 3
use sub as administrator
Alg:none
send request

![](images/lab2_alg_non_sub_aministrator.jpg)

![](images/lab2_my_account_request_with_modified_token.jpg)

step 4

now change to /admin and send request

![](images/lab2_aministrator_alg_none.jpg)

![](images/lab2_get_admin_request.jpg)

make sure alg : none

![](images/lab2_alog_non_administrator.jpg)

step 5
send GET /admin/delete?username=carlos

![](images/lab2_delete_carlos_account.jpg)

![](images/lab2_solved_lab.jpg)




