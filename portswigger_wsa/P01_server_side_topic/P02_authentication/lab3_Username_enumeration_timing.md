# Lab: Username enumeration via response timing

open burpsuite enter Your credentials: `wiener:peter`
it is default given in lab instruction

when you will try to enter different username and passsword your ip will block for 30 min after that 400 bad request occur to fix his we need to spoof our ip address

_X-Forwarded-For_ header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection
so set _X-Forwarded-For_: 10 , you can put any random value

default password we will wnter too long to get response time
eg- password=_peterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeter_
Set the max fraction digits to 0. This will be used to spoof your IP.
Select payload set 2 and

---

1.  With Burp running, submit an invalid username and password, then send the `POST /login` request to Burp Repeater. Experiment with different usernames and passwords. Notice that your IP will be blocked if you make too many invalid login attempts.
2.  Identify that the `X-Forwarded-For` header is supported, which allows you to spoof your IP address and bypass the IP-based brute-force protection.
3.  Continue experimenting with usernames and passwords. Pay particular attention to the response times. Notice that when the username is invalid, the response time is roughly the same. However, when you enter a valid username (your own), the response time is increased depending on the length of the password you entered.
4.  Send this request to Burp Intruder and select the attack type to **Pitchfork**. Clear the default payload positions and add the `X-Forwarded-For` header.
5.  Add payload positions for the `X-Forwarded-For` header and the `username` parameter. Set the password to a very long string of characters (about 100 characters should do it).
6.  On the **Payloads** tab, select payload set 1. Select the **Numbers** payload type. Enter the range 1 - 100 and set the ### stepto 1. Set the max fraction digits to 0. This will be used to spoof your IP.
7.  Select payload set 2 and add the list of usernames. Start the attack.
8.  When the attack finishes, at the top of the dialog, click **Columns** and select the **Response received** and **Response completed** options. These two columns are now displayed in the results table.
9.  Notice that one of the response times was significantly longer than the others. Repeat this request a few times to make sure it consistently takes longer, then make a note of this username.
10. Create a new Burp Intruder attack for the same request. Add the `X-Forwarded-For` header again and add a payload position to it. Insert the username that you just identified and add a payload position to the `password` parameter.
11. On the **Payloads** tab, add the list of numbers in payload set 1 and add the list of passwords to payload set 2. Start the attack.
12. When the attack is finished, find the response with a `302` status. Make a note of this password.
13. Log in using the username and password that you identified and access the user account page to solve the lab.

---

after getting username and password
intercept on to url

X-Forwarded-For: 60 or any random value to bypass login after 30 min.

username=oracle&password=michelle

send foword and intercept off
boom you solve the lab
