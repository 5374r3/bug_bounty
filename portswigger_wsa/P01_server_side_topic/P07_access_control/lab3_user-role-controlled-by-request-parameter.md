# User role controlled by request parameter

## This lab has an admin panel at `/admin`, which identifies administrators using a forgeable cookie.

## Solve the lab by accessing the admin panel and using it to delete the user `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login in using user and password  `wiener:peter`

https://0a1f00cd03ac9910c1294f51007200ae.web-security-academy.net/my-account?id=wiener

![screenshot](./images/lab3_admin_false.png)

intercept my account

![screenshot](./images/lab3_my_account_intercept.png)

change Admin=true

send forword

![screenshot](./images/lab3_admin_page_intercept.png)

Admin=true
and forword

![screenshot](./images/lab3_delete_carlos.png)

intercept on carlos delete selection

![screenshot](./images/lab3_delete_carlos_intercept.png)

Admin=true
forword request
