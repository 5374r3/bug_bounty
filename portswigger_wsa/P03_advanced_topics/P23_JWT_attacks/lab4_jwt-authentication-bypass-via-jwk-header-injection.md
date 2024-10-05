# JWT authentication bypass via jwk header injection

## This lab uses a JWT-based mechanism for handling sessions. The server supports the `jwk` parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

## To solve the lab, modify and sign a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

---

step 1

login in to account send to repeater

![](images/lab4_my_account.jpg)

click on json web token tab for header and payload

![](images/lab4_json_web_token_my_account.jpg)

step 2

![](images/lab4_RSA_key_generate.jpg)

step 3
in sub replace wiener with administrator
at the bottom click on attack click on embedded jwk
click on ok
you will notice jwk added into payload

send request 200k

![](images/lab4_sigining_rsa_key.jpg)

when you will get 200 ok go to bottom
you will see admin panel and wiener and carlos account delete operation

![](images/lab4_admin_panel.jpg)

step 4

send GET /admin/delete?username=carlos request to solve lab

![](images/lab4_delete_carlos_account.jpg)

![](images/lab4_solved_lab.jpg)
