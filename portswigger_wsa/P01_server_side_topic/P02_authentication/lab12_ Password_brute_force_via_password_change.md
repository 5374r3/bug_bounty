#  Password brute-force via password change

## This lab's password change functionality makes it vulnerable to brute-force attacks. To solve the lab, use the list of candidate passwords to brute-force Carlos's account and access his "My account" page.
- Your credentials: `wiener:peter`
- Victim's username: `carlos`
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)
___


when you enter wrong password with different password
like
currrent passwod = test1 => wrong password
new password = 123
confirm neew password = 1234
both new password and confirm new password must be wrong
if both new password and confirm password will be same you will redirect to login page again

![screenshot](images/lab12_pass_incorrect.jpg)

### step2

enter correct password
but new passwod and confirm password must be diffeernet

![screenshot](images/lab12_password_not_match.jpg)

![screenshot](images/lab12_grep_math.jpg)

note: important password and new password must be differnent

![screenshot](images/lab12_payload_position.jpg)

![screenshot](images/lab12_payload_result.jpg)
