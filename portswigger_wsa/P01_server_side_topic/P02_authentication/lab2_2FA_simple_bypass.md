# 2FA simple bypass

## This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

- Your credentials: `wiener:peter`
- Victim's credentials `carlos:montoya`

___


1.  Log in to your own account. Your 2FA verification code will be sent to you by email. Click the **Email client** button to access your emails.
2.  Go to your account page and make a note of the URL.
3.  Log out of your account.
4.  Log in using the victim's credentials.
5.  When prompted for the verification code, manually change the URL to navigate to `/my-account`. The lab is solved when the page loads.

https://0a1c007b048e344bc09e4a0000270042.web-security-academy.net/my-account?id=wiener
to bypass _2FA_ just change my_accound id

https://0a1c007b048e344bc09e4a0000270042.web-security-academy.net/my-account?id=carlos
