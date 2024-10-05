# JWT authentication bypass via jwk header injection

## This lab uses a JWT-based mechanism for handling sessions. The server supports the `jwk` parameter in the JWT header. This is sometimes used to embed the correct verification key directly in the token. However, it fails to check whether the provided key came from a trusted source.

## To solve the lab, modify and sign a JWT that gives you access to the admin panel at `/admin`, then delete the user `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

---

step 1

login in to account send to repeater

![[lab4_my_account.png]]

click on json web token tab for header and payload

![[lab4_json_web_token_my_account.png]]

step 2

![[lab4_RSA_key_generate.png]]

step 3
in sub replace wiener with administrator
at the bottom click on attack click on embedded jwk
click on ok
you will notice jwk added into payload

send request 200k

![[lab4_sigining_rsa_key.png]]

when you will get 200 ok go to bottom
you will see admin panel and wiener and carlos account delete operation

![[lab4_admin_panel.png]]

step 4

send GET /admin/delete?username=carlos request to solve lab

![[lab4_delete_carlos_account.png]]

![[portswigger_wsa/P03_advanced_topics/P23_JWT_attacks/images/lab4_solved_lab.png]]
