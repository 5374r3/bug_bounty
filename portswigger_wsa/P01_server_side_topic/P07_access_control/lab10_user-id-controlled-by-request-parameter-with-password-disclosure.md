# User ID controlled by request parameter with password disclosure

## This lab has user account page that contains the current user's existing password, prefilled in a masked input.

## To solve the lab, retrieve the administrator's password, then use it to delete `carlos`.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login using user id and password
click on my account
https://0a28008d04a82544c1485d8c00a1007e.web-security-academy.net/my-account?id=wiener

change wiener to administrator

https://0a28008d04a82544c1485d8c00a1007e.web-security-academy.net/my-account?id=administrator

click on password update and intercept
note down password
_acvjwk3utlwuhkrl6ens_
login using administratorid and password

go to admin panel and delete carlos account
lab solved
