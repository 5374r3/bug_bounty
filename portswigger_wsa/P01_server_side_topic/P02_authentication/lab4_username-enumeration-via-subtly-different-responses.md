# Lab: Username enumeration via subtly different responses

## This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

- [Candidate usernames](https://portswigger.net/web-security/authentication/auth-lab-usernames)
- [Candidate passwords](https://portswigger.net/web-security/authentication/auth-lab-passwords)

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page

___

2.  With Burp running, submit an invalid username and password. Send the `POST /login` request to Burp Intruder and add a payload position to the `username` parameter.
3.  On the **Payloads** tab, make sure that the **Simple list** payload type is selected and add the list of candidate usernames.
4.  On the **Options** tab, under **Grep - Extract**, click **Add**. In the dialog that appears, scroll down through the response until you find the error message `Invalid username or password.`. Use the mouse to highlight the text content of the message. The other settings will be automatically adjusted. Click **OK** and then start the attack.
5.  When the attack is finished, notice that there is an additional column containing the error message you extracted. Sort the results using this column to notice that one of them is subtly different.
6.  Look closer at this response and notice that it contains a typo in the error message - instead of a full stop/period, there is a trailing space. Make a note of this username.
7.  Close the attack and go back to the **Positions** tab. Insert the username you just identified and add a payload position to the `password` parameter:
    
    `username=identified-user&password=§invalid-password§`
8.  On the **Payloads** tab, clear the list of usernames and replace it with the list of passwords. Start the attack.
9.  When the attack is finished, notice that one of the requests received a `302` response. Make a note of this password.
10.  Log in using the username and password that you identified and access the user account page to solve the lab.

**NOTE:** in Grep - Extract Match `Invalid username or password.` don' t forget to add dot (`.`) 

