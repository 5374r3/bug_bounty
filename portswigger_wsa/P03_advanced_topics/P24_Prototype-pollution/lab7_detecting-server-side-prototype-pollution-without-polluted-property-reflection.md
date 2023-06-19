
# Detecting server-side prototype pollution without polluted property reflection

## This lab is built on Node.js and the Express framework. It is vulnerable to server-side [prototype pollution](https://portswigger.net/web-security/prototype-pollution) because it unsafely merges user-controllable input into a server-side JavaScript object.

To solve the lab, confirm the vulnerability by polluting `Object.prototype` in a way that triggers a noticeable but non-destructive change in the server's behavior. As this lab is designed to help you practice non-destructive detection techniques, you don't need to progress to exploitation.

You can log in to your own account with the following credentials: `wiener:peter`

___

step 1

login to account 
go to http history you will see `/my-account/change-address`
send to repeater you will get json object of user

![[lab7_json_object_with_user_information_repeater.png]]


step 2

```
"__proto__": {
    "foo":"bar"
}
```

![[lab7_change_address_proto_foo_bar.png]]

step 3

remove comma from json object to create error
and then send request you get 500 error with 400 status

![[lab7_satatus_400_remove_comma.png]]

step 4

```
"__proto__": {
 "status":555,
}
```


![[lab7_add_status_proto_555.png]]


step 5

```
"__proto__": {
 "isAdmin":true
}
```

![[lab7_add_is_admin_true_json.png]]


step 6

remove comma from json and send request 
you will notice status:555 in response
go to browser you will see lab solved

![[lab7_ststus_555_in_response.png]]

![[portswigger_wsa/P03_advanced_topics/P24_Prototype-pollution/images/lab7_solved_lab.png]]
